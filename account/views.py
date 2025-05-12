from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import SignInForm, TicketForm

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
  
  form = TicketForm()
  
  if request.method == 'POST':
    form = TicketForm(request.POST, request.FILES)
    if form.is_valid():  
      
      instance = form.save(commit=False)
      instance.username_ticket = request.user  # Assign the current user
      instance.save()
      messages.info(request, 'New ticket has been created')
      return redirect('dashboard')
  
  context = { 'form': form }
  return render(request, 'dashboard.html', context)

