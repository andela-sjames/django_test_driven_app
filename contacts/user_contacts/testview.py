from django.template.loader import render_to_string
from django.test import TestCase, Client
from user_contacts.models import Person, Phone
from user_contacts.views import *

# Create your tests here

class ViewTest(TestCase):

    def setUp(self):
        self.client_stub = Client()

    def test_view_home_route(self):
      response = self.client_stub.get('/')
      self.assertEquals(response.status_code, 200)

    def test_view_contacts_route(self):
      response = self.client_stub.get('/all/')
      self.assertEquals(response.status_code, 200)

    def test_add_contact_route(self):
      response = self.client_stub.get('/add/')
      self.assertEqual(response.status_code, 200)

