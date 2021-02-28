'''Countries, States, Cities and Neighborhoods modesl'''

import uuid

#Django
from django.db import models

class Countries(models.Model):
    '''countries Model'''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class States(models.Model):
    '''States Model'''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, null=False, blank=False)
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.country_id}'


class Cities(models.Model):
    '''Cities Model'''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, null=False, blank=False)
    state_id = models.ForeignKey(States, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.state_id}'


class Neighborhoods(models.Model):
    '''Neighborhoods Model'''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    city_id = models.ForeignKey(Cities, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.city_id}'


    