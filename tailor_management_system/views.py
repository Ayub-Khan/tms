"""Driver function."""

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import View


def dashboard(request):
    """Dashboard view."""
    template = loader.get_template('tailor_management_system/dashboard.html')
    return HttpResponse(template.render({}, request))
