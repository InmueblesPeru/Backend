"""Users Urls"""

# Django
from django.urls import path

# Views
from users.views import (
    ProfileLoginApiView,
    ProfileSignUpView,
    ProfileView,
)

urlpatterns = [
    path('users/login/', ProfileLoginApiView.as_view(), name='login'),
    path('users/signup/', ProfileSignUpView.as_view(), name='signup'),
    path('users/profile/', ProfileView.as_view(), name='profile'),
]
