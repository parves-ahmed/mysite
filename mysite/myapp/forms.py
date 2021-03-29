from django import forms
from django.forms import ClearableFileInput

from .models import Trainings, CoverImage


class TrainingForm(forms.ModelForm):

    class Meta:
        model = Trainings
        fields = '__all__'


class UploadCoverImage(forms.ModelForm):
    class Meta:
        model = CoverImage
        fields = ['photos']
        widgets = {
            'photos': ClearableFileInput(attrs={'multiple': True})
        }


