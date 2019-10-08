"""Driver function."""

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import View


class DashboardView(View):
    """Dashboard class based view."""

    def get(self, request):
        """Dashboard view."""
        template = loader.get_template(
            'tailor_management_system/dashboard.html')
        context = {'welcome_msg': 'Hello World!'}
        return HttpResponse(template.render(context, request))


dashboard_view = DashboardView.as_view()
