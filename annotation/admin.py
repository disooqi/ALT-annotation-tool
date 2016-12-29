from django.contrib import admin

# Register your models here.

from .models import Token, Tweet, TokenOccurrence

admin.site.register(Token)
admin.site.register(Tweet)
admin.site.register(TokenOccurrence)
