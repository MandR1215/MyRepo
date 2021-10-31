import numpy as np
import pickle, sys, os
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder

sys.path.append(os.path.abspath(".") + '/myapp/pkl_files')

def process(csv):
    # data
    df = pd.read_csv(csv)

    # pickles
    path = os.path.abspath('./myapp/pkl_files')
    with open(path+'/subset1.pkl', 'rb') as f:
         subset1 = pickle.load(f)
    with open(path+'/subset2.pkl', 'rb') as f:
         subset2 = pickle.load(f)
    with open(path+'/subset3.pkl', 'rb') as f:
         subset3 = pickle.load(f)
    with open(path+'/subset4.pkl', 'rb') as f:
         subset4 = pickle.load(f)
    with open(path+'/labels.pkl', 'rb') as f:
         labels = pickle.load(f)
    with open(path+'/model.pkl', 'rb') as f:
         model = pickle.load(f)

    # get id column
    id_column = df['お仕事No.']

    # set columns
    df = df.drop(['お仕事No.'], axis=1)
    df = df[subset1]
    print(df.info())
    df = df.drop(subset2, axis=1)
    print(df.info())
    encoder = LabelEncoder()
    for label in labels:
        df[label] = encoder.fit(df[label]).transform(df[label])
    print(df.describe())
    df = df[subset3]
    print(df.info())
    df = df.fillna(0)
    df = df.drop(labels=subset4, axis=1)
    print(df.info())
    df= (df - df.min()) / (df.max() - df.min())
    print(df.info())

    # prediction
    pred = model.predict(np.array(df))
    result = pd.concat([id_column, pd.DataFrame(pred.T, columns=['応募数 合計'])], axis=1)
    print(result)

    # make csv
    result.to_csv(path + '/out.csv', index=False)
    return result
