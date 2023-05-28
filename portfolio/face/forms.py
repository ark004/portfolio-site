from django import forms
from .models import face

class ImageForm(forms.ModelForm):
    class Meta:
        model = face
        fields = '__all__'
        labels = {'images':'photo'}