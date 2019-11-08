"""Views for tailor management system application."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import loader
from django.views import View


class DashboardView(LoginRequiredMixin, View):
    """Dashboard class based view."""

    def get(self, request):
        """Dashboard view."""
        template = loader.get_template(
            'tailor_management_system/dashboard.html')
        return HttpResponse(template.render(request=request))


dashboard_view = DashboardView.as_view()
