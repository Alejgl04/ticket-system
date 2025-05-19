from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth.models import auth

from ticket.models import Ticket
from .forms import SignInForm, TicketForm

# Create your views here.

# THIS VIEWS FUNCTIONS ARE FOR FINAL USER THAT WANT TO ACCESS TO TICKET SYS#

@login_required(login_url='index')
def get_ticketby_id(request, ticket_id):
  ticket = Ticket.objects.get(pk=ticket_id)
  return render(request, 'ticket-by-id.html', {'ticket':ticket})


@login_required(login_url='index')
def profile_username(request):
  
  return render (request, 'profile.html', {'username': request.user})

@login_required(login_url='index')
def getTickets(request):
  tickets = Ticket.objects.filter(username_ticket=request.user)
  return render(request, 'tickets.html', { 'tickets':tickets })


@login_required(login_url='index')
def dashboard(request):
  
  form = TicketForm()
  
  if request.method == 'POST':
    form = TicketForm(request.POST, request.FILES)
    if form.is_valid():  
      
      instance = form.save(commit=False)
      instance.username_ticket = request.user  # Assign the current user
      instance.save()
      messages.success(request, 'New ticket has been created successfully')

      return redirect('dashboard')
  
  context = { 'form': form }
  return render(request, 'dashboard.html', context)

def index(request):
  if request.user.is_authenticated:
    return redirect('dashboard')
  
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

