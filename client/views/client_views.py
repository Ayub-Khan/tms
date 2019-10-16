"""All the views."""

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from rest_framework.views import View

from client.forms import ClientForm
from client.models import Client
from client.utils import get_measurements


class ClientListView(View):
    """Class based view for Client for listing all the clients."""

    def get(self, request):
        """Render client list tempalte.."""
        clients = Client.objects.all()
        template = loader.get_template('client/list-clients.html')
        context = {
            'clients': clients,
        }
        return HttpResponse(template.render(context, request))


client_list_view = ClientListView.as_view()


class ClientDetailView(View):
    """Class based view for displaying client detail."""

    def get(self, request, pk, format=None):
        """Get client details by id ."""
        template = loader.get_template('client/client-detail.html')
        client = get_object_or_404(Client, id=pk)
        measurements, measurements_exist = get_measurements(pk, client)
        context = {
            'client': client,
            'measurements': measurements,
            'measurements_exist': measurements_exist,
            'is_male': client.gender == 'M',
        }
        return HttpResponse(template.render(context, request))


client_detail_view = ClientDetailView.as_view()


class ClientDeleteView(View):
    """Class based view for displaying client detail."""

    def get(self, request, pk, format=None):
        """Delete client by id ."""
        client_to_delete = get_object_or_404(Client, id=pk)
        client_to_delete.delete()
        return redirect('client:clients')


client_delete_view = ClientDeleteView.as_view()


class ClientAddView(View):
    """Class based view for adding new."""

    def get(self, request):
        """Return add new client form."""
        form = ClientForm()
        return render(request, 'client/add-client.html',
                      {'form': form, 'func': 'Add'})

    def post(self, request):
        """Save client and redirect to index."""
        form = ClientForm(request.POST)
        if form.is_valid():
            new_client = form.save()
            return redirect('client:measurment_add', client_id=new_client.id)
        else:
            return render(request, 'client/add-client.html', {'form': form})


client_add_view = ClientAddView.as_view()


class ClientUpdateView(View):
    """Class based view for displaying client detail."""

    def get(self, request, pk):
        """Return update client form."""
        client = get_object_or_404(Client, id=pk)
        form = ClientForm(instance=client)
        return render(request, 'client/add-client.html',
                      {'form': form,
                       'func': 'Update'})

    def post(self, request, pk):
        """Update client by id ."""
        client = get_object_or_404(Client, id=pk)
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            redirect('client:clients')
        else:
            return render(request, 'client/add-client.html', {'form': form})


client_update_view = ClientUpdateView.as_view()
