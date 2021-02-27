"""Users Urls"""

# Django
from django.urls import path

# Views
from users.views import ProfileLoginApiView

urlpatterns = [
    path('users/login/', ProfileLoginApiView.as_view(), name='login'),
]
