from .models import Admin_model
from django import forms 

class My_form(forms.ModelForm):
    class Meta:
        model=Admin_model
        fields="__all__"