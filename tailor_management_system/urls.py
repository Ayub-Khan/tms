"""urls for application."""

from django.urls import path

from . import views
from client import views as client_views
from tailor_management_system.views import dashboard_view

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', client_views.index_view, name='index'),
    path('<int:pk>/', client_views.client_detail_view, name='detail'),
    path('client/', client_views.clientView, name='client'),
    path('edit/<int:pk>/', client_views.edit, name='edit'),
    path('delete/<int:pk>/', client_views.delete, name='delete')
]
