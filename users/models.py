from django.db import models

from django.contrib.home.models import AbstractUser

class CustomUser(AbstractUser):
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username']
    username = models.CharField(blank=True, max_length=254,)
    email = models.EmailField(blank=False, max_length=254, unique=True, verbose_name="Email Address",)
    

