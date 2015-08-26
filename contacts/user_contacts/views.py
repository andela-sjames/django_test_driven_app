from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from user_contacts.models import Phone, Person
from user_contacts.new_contact_form import ContactForm

def home(request):
    return render_to_response('index.html')

def all_contacts(request):
    contacts = Phone.objects.all()
    return render_to_response('all.html', {'contacts':contacts})

def add(request):
    person_form = ContactForm()
    return render(request, 'add.html', {'person_form' : person_form}, context_instance = RequestContext(request))



