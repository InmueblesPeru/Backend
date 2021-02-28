""" Property model"""

import uuid

# Django
from django.db import models

# Apps
from locations.models.countries import Neighborhoods

# Utils
from utils.models import DateModels


class Property(models.Model):
    """Properties model"""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_neighborhood = models.ForeignKey(Neighborhoods, on_delete=models.CASCADE)
    number_rooms = models.PositiveIntegerField(default=0)
    number_bathrooms = models.PositiveIntegerField(default=0)
    area = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    status = models.BooleanField(default=1)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='properties/photos')

    def __str__(self):
        return self.title
    

