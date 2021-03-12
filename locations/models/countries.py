"""Countries, States, Cities and Neighborhoods models"""

# Django
from django.db import models


class Countries(models.Model):
    """countries Model"""

    name = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.name


class States(models.Model):
    """States Model"""

    name = models.CharField(max_length=60, null=False, blank=False)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.country}'


class Cities(models.Model):
    """Cities Model"""

    name = models.CharField(max_length=60, null=False, blank=False)
    state = models.ForeignKey(States, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.state}'


class Neighborhoods(models.Model):
    """Neighborhoods Model"""

    name = models.CharField(max_length=60, null=False, blank=False)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.city}'
