from django.db import models


class properties (models.Model):
    """Properties Model"""
    
    description = models.CharField(max_length=250)


