from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django import forms
from ticket.models import Ticket

class SignInForm(AuthenticationForm):
  
  username = forms.CharField(widget=TextInput(), strip=False)
  password = forms.CharField(widget=PasswordInput())
  
  
class TicketForm(forms.ModelForm):
  title = forms.CharField(widget=forms.TextInput(attrs={'class':'border-1','placeholder':'Enter your issue'}))
  description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder':'A little bit of your problem'}))
  image = forms.FileField(
    label="",
    required = False,
    widget=forms.FileInput(attrs={'class':'cursor-pointer relative block opacity-0 w-full h-full p-20 z-50','placeholder':'Drop files anywhere to upload'}))

  class Meta:
    model = Ticket
    fields = ['title', 'description','image']
    exclude = ['user']
    