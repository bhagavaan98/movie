from django import forms
from application.models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields="__all__"