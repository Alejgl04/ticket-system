

from django.test import TestCase,Client

from django.urls import reverse

from django.contrib.auth import get_user_model

from .models import Ticket, TicketStatus
from .forms import TicketForm


# Create your tests here.

USER_MODEL = get_user_model()

class TicketTestCase(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    cls.client = Client()
    cls.url = reverse('dashboard')
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
    
  def test_get_dashboard(self):
    """ Tests that a GET request works and renders the correct template"""

    self.client.force_login(self.user)
    response = self.client.get(self.url)

    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'dashboard.html')
  
  def test_user_must_be_logged_in(self):

      response = self.client.get(self.url)
      self.assertEqual(response.status_code, 302)
      
      
  def test_form_fields(self):
    """ Tests that only title and body fields are displayed in the user form"""
    form_data = {'title': 'something', 'description': 'abc23'}
    form = TicketForm(data=form_data)
    self.assertTrue(form.is_valid())
    self.assertEqual(form.cleaned_data['title'], 'something')

  def test_invalid_form(self):
    form_data = {'title': '', 'description': 'abc'}
    form = TicketForm(data=form_data)
    self.assertFalse(form.is_valid())
    self.assertIn('title', form.errors)