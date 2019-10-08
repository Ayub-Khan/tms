"""urls for application."""

from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^dashboard/$', views.dashboard, name='dashboard')
]
