import re
from django import forms
from django.core.exceptions import ValidationError
from user_contacts.models import Person, Phone

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    country = forms.CharField(required=False)
    number = forms.CharField(max_length=10)

    def save(self):
        if self.is_valid():
            data = self.cleaned_data
            person = Person.objects.create(first_name=data.get('first_name'), last_name=data.get('last_name'),
                email=data.get('email'), address=data.get('address'), city=data.get('city'), state=data.get('state'),
                country=data.get('country'))
            phone = Phone.objects.create(person=person, number=data.get('number'))
            return phone

            