from django import forms
from .models import UploadedDocument

class UploadPDFForm(forms.ModelForm):
    class Meta:
        model = UploadedDocument
        fields = ['title', 'file']  # include whatever fields your model has
