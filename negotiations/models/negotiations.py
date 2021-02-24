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

    """ Negotiations choices """
    
    STATUS_CHOICE = [
        (0, 'NO_NEGOTIATION'),
        (1, 'OPEN_NEGOTIATION'),
        (2, 'CLOSE_NEGOTIATION'),    
    ]

    type_user = models.IntegerField(choices=STATUS_CHOICE, default=0)
