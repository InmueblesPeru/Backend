"""users views"""

# Django REST Framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Serializers
from users.serializers import UserLoginSerializer


class UserLoginApiView(APIView):
    """User login API view"""

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()

        data = {
            'status': 'ok',
            'token': token
        }

        return Response(data, status=status.HTTP_201_CREATED)
