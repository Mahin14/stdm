from django import forms
from .models import *

class studentclasscreate(forms.ModelForm):
    class Meta:
        model=StudentClass
        fields='__all__'

        label={
            'class_name':'Class Name',        }




class teacherCreationform(forms.ModelForm):
        birthDate=forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
        # className=forms.BooleanField( )
        class Meta:
            model=teachers
            fields='__all__'
            label={
            'first_name':'First Name',
            'last_name':'Last Name',
            'birthDate':'Date of Birth',
            'phoneNumber':'Mobile Phone no',
                 }

class CreteNotice(forms.ModelForm):
    class Meta:
        model=school_notice
        fields=['notice_subject','motice_details']
        label={
            'notice_subject':'NOTICE SUBJECT',
            'notice_details':'NOTICE DETAILS'
        }
