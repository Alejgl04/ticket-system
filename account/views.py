from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

from .forms import SignInForm

# Create your views here.

# THIS VIEWS FUNCTIONS ARE FOR FINAL USER THAT WANT TO ACCESS TO TICKET SYS#
def index(request):
  form = SignInForm()
  
  if request.method == 'POST':
    
    form = SignInForm(request, data=request.POST)
    
    if form.is_valid():
      
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request, username=username, password=password)
      
      if user is not None:
        
        auth.login(request, user)
        return redirect('dashboard')
      
  context = { 'form': form }
  return render(request, 'sign-in.html', context=context)

def sign_out(request):
  
  auth.logout(request)  
  return redirect('index')


@login_required(login_url='index')
def dashboard(request):
  return render(request, 'dashboard.html')