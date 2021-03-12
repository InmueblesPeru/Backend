"""users views"""

# Django REST Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from users.models.users import Profile

# Serializers
from users.serializers import (
    ProfileLoginSerializer,
    ProfileModelSerializer,
    ProfileSignUpSerializer
)


class ProfileLoginApiView(APIView):
    """User login API view"""

    def post(self, request, *args, **kwargs):
        serializer = ProfileLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()

        data = {
            'user': ProfileModelSerializer(user).data,
            'access_token': token
        }

        return Response(data, status=status.HTTP_201_CREATED)


class ProfileSignUpView(APIView):
    """User Sign Up API view"""

    def post(self, request, *args, **kwargs):
        serializer = ProfileSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = ProfileModelSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)


class ProfileView(APIView):

    def get(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass
