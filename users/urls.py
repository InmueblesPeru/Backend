"""Users Urls"""

# Django
from django.urls import path

# Views
from users.views import (
    ProfileLoginApiView,
    ProfileSignUpView
)

urlpatterns = [
    path('users/login/', ProfileLoginApiView.as_view(), name='login'),
    path('users/signup/', ProfileSignUpView.as_view(), name='signup'),
]
