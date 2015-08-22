from django.contrib import admin
from user_contacts.models import Person, Phone

# Register your models here.
admin.site.register(Person)
admin.site.register(Phone)
