from django import forms
from .models import Gateway

class PostForm(forms.ModelForm):
    class Meta:
        model=Gateway
        fields='__all__'