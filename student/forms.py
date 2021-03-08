from django import forms
from django.db.models import fields
from .models import *


class studentcreateform(forms.ModelForm):
    # birthDate=forms.DateTimeField(widget = forms.SelectDateWidget)
    birthDate=forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=students
        fields="__all__"
        label={
            'registration_no':'registration NO',
            'name':'name',
            'photo':'Photo',
                }

class gardianInfoForm(forms.ModelForm):
    class Meta:
        model=GuardianInfo
        fields=('father_name','father_phone_no','father_occupation','father_yearly_income','mother_name','mother_phone_no','mother_ocupation','mother_yearly_income','guardian_name','guadian_phone_no','relationship_with_student')
        label={}


class PreviousAcademicInfoForm(forms.ModelForm):
    class Meta:
        model=PreviousAcademicInfo
        fields=('institute_name','name_of_exam','group','gpa','board_roll','passing_year')
        label={}

