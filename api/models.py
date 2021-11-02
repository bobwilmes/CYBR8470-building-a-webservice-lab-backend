from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')

# Add Dog and Breed to models.py 11-1-2021
# Add value choices for breed characteristics
ONE   = 1
TWO   = 2
THREE = 3
FOUR  = 4
FIVE  = 5 
VALUE_CHOICES = (
  (ONE, 'One'),
  (TWO, 'Two'),
  (THREE, 'Three'),
  (FOUR, 'Four'),
  (FIVE, 'Five'),
)

class Breed(models.Model):
    BREED_SIZE = (
      ('T', 'Tiny'),
      ('S', 'Small'),
      ('M', 'Medium'),
      ('L', 'Large'),
    )
    name           = models.CharField(max_length=30)
    size           = models.CharField(max_length=1,choices=BREED_SIZE)
    friendliness   = models.IntegerField(default=0,choices=VALUE_CHOICES)
    trainability   = models.IntegerField(default=0,choices=VALUE_CHOICES)
    sheddingamount = models.IntegerField(default=0,choices=VALUE_CHOICES)
    exersizeneeds  = models.IntegerField(default=0,choices=VALUE_CHOICES)

class Dog(models.Model):
    GENDER_CHOICES = (
      ('M', 'Male'),
      ('F', 'Female'),
      ('X', 'Other'),
    )
    name   = models.CharField(max_length=30)
    age    = models.IntegerField(default=0)
    breed  = models.ForeignKey(Breed,on_delete=models.CASCADE) 
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    color  = models.CharField(max_length=30)
    favoritefood = models.CharField(max_length=30)
    favoritetoy  = models.CharField(max_length=30)      
 

  


