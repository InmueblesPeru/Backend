"""User Admin"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Models
from users.models.users import Profile


@admin.register(Profile)
class ProfileAdmin(UserAdmin):

    list_display = ('username', 'first_name', 'last_name','email', 'phone_number', 'type_user',)

