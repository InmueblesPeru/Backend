"""Properties Urls"""

# Django
from django.urls import path

# Views
from properties.views import ListProperties

urlpatterns = [
    path('properties/', ListProperties.as_view()),
]
