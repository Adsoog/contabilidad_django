# forms.py
from django import forms

class UploadFileForm(forms.Form):
    archivo = forms.FileField()