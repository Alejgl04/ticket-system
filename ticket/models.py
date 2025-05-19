from django.db import models

from django.contrib.auth.models import User

class TicketStatus(models.TextChoices):
  TO_DO = 'To Do'
  IN_PROGRESS = 'In Progress'
  IN_REVIEW = 'In Review'
  DONE = 'Done'

class Ticket(models.Model):
  
  title = models.CharField(max_length=100)
  description = models.TextField()
  status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
  assigned = models.ForeignKey(
    User, 
    null=True, 
    blank=True, 
    on_delete=models.CASCADE, 
    limit_choices_to={'is_staff': True}
  )
  username_ticket = models.ForeignKey(
    User, 
    on_delete=models.CASCADE, 
    limit_choices_to={'is_staff': False}, 
    related_name="username_ticket", 
    related_query_name="username_ticket",
    null=True, 
    blank=True, 
    
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)  
  image = models.ImageField(upload_to='images/', null=True, blank=True)
  
  def get_status_class(self):
    if self.status == TicketStatus.TO_DO:
        return 'badge badge-primary'
    elif self.status == TicketStatus.IN_PROGRESS:
        return 'badge badge-secondary'
    elif self.status == TicketStatus.IN_REVIEW:
        return 'badge badge-info'
    elif self.status == TicketStatus.DONE:
        return 'badge badge-success'
    else:
      return 'badge badge-primary'
  