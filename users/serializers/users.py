"""Profile serializers"""

# Django
from django.contrib.auth import authenticate, password_validation

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.core.validators import RegexValidator
from rest_framework.validators import UniqueValidator

# Models
from users.models.users import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer"""
    class Meta:
        """Meta class"""

        model = Profile
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )


class ProfileLoginSerializer(serializers.Serializer):
    """Profile login serializer"""

    email = serializers.EmailField()
    password = serializers.CharField(
        min_length=8,
        max_length=64
    )

    def validate(self, data):
        """check credentials"""

        user = authenticate(username=data['email'], password=data['password'])

        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        """generate or retrieve a new token"""

        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class ProfileSignUpSerializer(serializers.Serializer):
    """Profile Sign Up Serializer"""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Profile.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=Profile.objects.all())]
    )

    # Phone Number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
    )
    phone_number = serializers.CharField(validators=[phone_regex])

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):

        passwd = data['password']
        passwd_confirmation = data['password_confirmation']

        if passwd != passwd_confirmation:
            raise serializers.ValidationError("Passwords don't match")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle Profile Creation"""

        data.pop('password_confirmation')
        user = Profile.objects.create_user(**data)
        return user

