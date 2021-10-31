from django import forms

class UploadForm(forms.Form):
    file = forms.FileField(label='CSVファイル', required=True, widget=forms.widgets.FileInput)
