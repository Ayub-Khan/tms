"""Initiat File."""

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    """Initiat File."""
    return HttpResponse("Hello World. Polls Index.")
