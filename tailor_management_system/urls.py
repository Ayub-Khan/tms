"""urls for tms application."""

from django.urls import path

from . import views
from tailor_management_system.views import dashboard_view

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard')
]
