"""urls for client application."""

from django.urls import path

from client.views import client_view, client_detail_view

urlpatterns = [
    path('clients/', client_view, name='clients'),
    path('clients/<int:pk>/', client_detail_view, name='client_detail')
]
