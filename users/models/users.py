""" User model"""

# Django 
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User (AbstractBaseUser):
    """User profile model extends of AbstractBaseUser and PermissionsMixin"""

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'Error, email already registred'
        }
    )

    phone = models.TextField(max_length=15, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


    def __str__(self):
        return self.username