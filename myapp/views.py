from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from .forms import UploadForm
from .functions import process
import os, csv


def index(request):
    params = {'uploadForm': UploadForm(), 'download': False}
    if (request.method == 'POST'):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # process
            result = process(request.FILES['file'])
            print(result)
            params['download'] = True

    return render(request, 'myapp/index.html', params)

def download(request):
    filename, filepath = 'out.csv', '/home/IriesSeis/iriesseis.pythonanywhere.com/myapp/pkl_files/out.csv'
    return FileResponse(open(filepath, "rb"), as_attachment=True, filename=filename)

    # path = os.path.abspath('./myapp/pkl_files')
    # with open(path+'/subset1.pkl', 'rb') as f:
    #     subset1 = pickle.load(f)
    #
    # return render(request, 'myapp/index.html')
