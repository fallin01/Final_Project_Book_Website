import datetime
from datetime import date
from django.db import models

from django.urls.base import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
  
    
    def __str__(self):
        return self.title

       