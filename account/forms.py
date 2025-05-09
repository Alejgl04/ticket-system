from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django import forms

class SignInForm(AuthenticationForm):
  
  username = forms.CharField(widget=TextInput(), strip=False)
  password = forms.CharField(widget=PasswordInput())