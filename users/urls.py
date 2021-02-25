"""Users Urls"""

# Django
from django.urls import path

# Views
from users.views import UserLoginApiView

urlpatterns = [
    path('users/login/', UserLoginApiView.as_view(), name='login'),
]
