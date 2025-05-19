from django.urls import path
from . import views

urlpatterns = [

  path('', views.index, name='index'),
  
  path('sign-out', views.sign_out, name='sign-out'),
  path('dashboard/profile', views.profile_username, name='profile'),
  
  path('dashboard', views.dashboard, name='dashboard'),
  path('dashboard/tickets', views.getTickets, name='tickets'),
  path('dashboard/ticket/<int:ticket_id>', views.get_ticketby_id, name='ticket-by-id'),

]