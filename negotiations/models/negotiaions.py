'''Negotiation model'''

import uuid

#Django
from django.db import models

#apps
from users.models.users import User
from properties,models.properties import Property


class Negotiation(models.Model):
    '''Negotiation Model'''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_property = models.ForeignKey(Property, on_delete=models.CASCADE)

    Class Status(models.IntegerChoices):
        '''Status Choice'''

        NO_NEGOTIATION = 0
        OPEN_NEGOTIATION = 1
        CLOSE_NEGOTIATION = 2

    status = models.IntegerField(choices=Status.choices)
