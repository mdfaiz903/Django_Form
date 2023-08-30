from typing import Any, Dict
from django import forms 
from . models import geekmodel
from django.core import validators
class INPUTFORM(forms.Form):
    first_name = forms.CharField(max_length=200,error_messages={'required':'Enter name must'})
    last_name = forms.CharField(max_length=200,)
    email = forms.EmailField(
        validators = [validators.MaxLengthValidator(30)]
        
    )
    roll_number = forms.IntegerField(
        help_text="Enter 6 digit roll number",
        min_value=1,
    )
    phone_number = forms.IntegerField(
       required=False,
       widget=forms.HiddenInput(),
       initial=+880
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        max_length=16,
        min_length=6,
    )
    con_password = forms.CharField(
        widget=forms.PasswordInput(),
        max_length=16,
        min_length=6,
    )
    texarea = forms.CharField(
        widget= forms.Textarea(attrs={'rows':5,'cols':23})

    )
    checkbox = forms.CharField(
        widget=forms.CheckboxInput()
    )
    payment = forms.DecimalField(
        min_value=2500,
        max_value=4000,
        max_digits=6,
        decimal_places=2,
    )
    Django = forms.BooleanField(
        
    )
# for password match 
    def clean(self):
        cleaned_data = super().clean()
        pass_match = cleaned_data.get('password')
        re_pass_match = cleaned_data.get('con_password')
        if pass_match != re_pass_match:
            raise forms.ValidationError('Password donesnot match')
        

        
class geekForm(forms.Form):
    model = geekmodel
    fields = '__all__'