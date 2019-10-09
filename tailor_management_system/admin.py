"""Admin for tailor management application."""

from django.contrib import admin
from client.models import Client

admin.site.register(Client)
# Register your models here.
