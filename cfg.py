'''Manage envinronment variables'''

from decouple import config

KEY = config('SECRET_KEY')
