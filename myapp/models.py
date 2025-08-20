from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.

import uuid
import os

def path_losts(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/losts', filename)

def path_founds(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/founds', filename)



class Lost(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    item = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    photo = models.ImageField(blank=True, upload_to=path_losts)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.item 
    
class Found(models.Model):
    
    item = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    photo = models.ImageField(blank=True, upload_to=path_founds)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.item 