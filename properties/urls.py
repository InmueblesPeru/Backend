"""Properties Urls"""

# Django
from django.urls import path

# Restframework
# from rest_framework.routers import DefaultRouter

# Views
from properties.views import ListProperties

#router = DefaultRouter()
#router.register(r'properties', ListProperties, basename='property')
#urlpatterns = router.urls

urlpatterns = [
    path('properties/', ListProperties.as_view()),
]
