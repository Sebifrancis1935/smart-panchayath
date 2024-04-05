from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User, Panchayath, Muncipality, Corporation


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['mail', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class PanchayathLoginForm(forms.ModelForm):
    class Meta:
        model = Panchayath
        fields = ['p_id', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class MuncipalityLoginForm(forms.ModelForm):
    class Meta:
        model = Muncipality
        fields = ['m_id', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class CorporationLoginForm(forms.ModelForm):
    class Meta:
        model = Corporation
        fields = ['c_id', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
