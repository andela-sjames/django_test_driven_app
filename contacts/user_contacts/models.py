from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(null = True, blank = True)
    address = models.TextField(null = True, blank = True)
    city = models.CharField(max_length = 15, null = True,blank = True)
    state = models.CharField(max_length = 15, null = True, blank = True)
    country = models.CharField(max_length = 15, null = True, blank = True)

    def __unicode__(self):
        return self.last_name +", "+ self.first_name

class Phone(models.Model):
    person = models.ForeignKey('Person')
    number = models.CharField(max_length=10)

    def __unicode__(self):
        return self.number