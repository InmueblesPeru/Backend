'''Negotiation model'''

import uuid

#Django
from django.db import models

#apps
from users.models.users import Profile
from properties.models.properties import Property


class Negotiation(models.Model):
    '''Negotiation Model'''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id_property = models.ForeignKey(Property, on_delete=models.CASCADE)

    # Negotiations choices
    NO_NEGOTIATION = 0
    OPEN_NEGOTIATION = 1
    CLOSE_NEGOTIATION = 2
    
    STATUS_CHOICE = [
        (NO_NEGOTIATION, 'No Negotiation'),
        (OPEN_NEGOTIATION, 'Open Negotiation'),
        (CLOSE_NEGOTIATION, 'Close Negotiation'),    
    ]

    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default=NO_NEGOTIATION,)
