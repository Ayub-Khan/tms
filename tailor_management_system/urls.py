"""urls for tms application."""

from django.urls import path

from tailor_management_system.views import dashboard_view

app_name = 'tailor_management_system'
urlpatterns = [
    path('', dashboard_view, name='dashboard')
]
