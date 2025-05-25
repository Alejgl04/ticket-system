from django.test import TestCase
from .models import Ticket, TicketStatus
from django.contrib.auth import get_user_model
from django.test import Client
# Create your tests here.

USER_MODEL = get_user_model()

class TicketTestCase(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    cls.user = USER_MODEL.objects.create_user(
      email='alexdoe@test.com',
      first_name='Alex',
      last_name='Doe',
      username='user123',
      password='password456'
    )
    cls.ticket = Ticket.objects.create(
      title='My first ticket',
      description='This is a description',
      status=TicketStatus.TO_DO,
      assigned=cls.user,
      username_ticket=cls.user,
  )
    
  def test_create_ticket(self):
    self.assertEqual(self.ticket.title, 'My first ticket')
    self.assertEqual(self.ticket.description, 'This is a description')
    self.assertEqual(self.ticket.status, TicketStatus.TO_DO )
    self.assertTrue(self.ticket.assigned, self.user.is_staff )
    self.assertEqual(self.ticket.username_ticket, self.user)