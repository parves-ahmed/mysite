from django import forms
from .models import Trainings


class TrainingForm(forms.ModelForm):

    class Meta:
        model = Trainings
        fields = '__all__'


