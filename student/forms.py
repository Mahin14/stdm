from django import forms
from .models import *


class studentcreateform(forms.ModelForm):
    # birthDate=forms.DateTimeField(widget = forms.SelectDateWidget)
    birthDate=forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=students
        fields='__all__'
        label={
            'registration_no':'registration NO',
            'name':'name',
            'photo':'Photo',
                }