"""Negotiation model"""

import uuid

#Django
from django.db import models

#apps
from users.models.users import Profile
from properties.models.properties import Property


class Negotiation(models.Model):
    """Negotiation Model"""

    id_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id_property = models.ForeignKey(Property, on_delete=models.CASCADE)

    """ Negotiations choices """
    
    STATUS_CHOICE = [
        (0, 'No Negotiation'),
        (1, 'Open Negotiation'),
        (2, 'Close Negotiation'),    
    ]

    type_user = models.IntegerField(choices=STATUS_CHOICE, default=0)
