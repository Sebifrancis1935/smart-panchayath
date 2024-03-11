from django import forms
from .models import User, Panchayath


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


class P_loginForm(forms.ModelForm):
    class Meta:
        model = Panchayath
        fields = '__all__'
