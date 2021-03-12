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
    path('api/v1/users/login/', ProfileLoginApiView.as_view(), name='login'),
    path('api/v1/users/signup/', ProfileSignUpView.as_view(), name='signup'),
    path('api/v1/users/profile/', ProfileView.as_view(), name='profile'),
]
