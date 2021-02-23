'''countries model'''

import uuid

#Django
from django.db import models

class Countries(models.Model):
    '''countries Model'''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):
        return self.name