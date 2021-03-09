""" User model"""

import uuid

# Django 
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utils
from utils.models import DateModels


class Profile (AbstractUser, DateModels):
    """Profile model
    
    proxy model that extends the base data with other information
    """

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    phone_number = models.CharField(validators=[phone_regex], max_length=17)

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'Error, already registered'
        }
    )

    """ Negotiations choices """
    
    STATUS_CHOICE = [
        (0, 'Unselected'),
        (1, 'Buyer'),
        (2, 'Seller'),    
    ]

    type_user = models.IntegerField(choices=STATUS_CHOICE, default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username
