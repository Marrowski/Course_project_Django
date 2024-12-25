from cProfile import label

from django import forms
from django.core.exceptions import ValidationError
from .models import *

def valid_name(value:str):
    if not value.istitle():
        raise ValidationError("Ім'я та прізвище мають починатись з великої літери")


class RegisterForm(forms.Form):
    name = forms.CharField(validators=valid_name, max_length=50, required=True, label='Ім`я користувача')
    surname = forms.CharField(validators=valid_name, max_length=50, required=False, label='Прізвище')
    email = forms.EmailField(required=True, label='Email')
    password = forms.PasswordInput()


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, label='Email')
    password = forms.PasswordInput()


