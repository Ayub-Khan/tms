"""All the views."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import View

from client.forms import ClientForm
from client.models import Client
from client.utils import get_measurements
from order.models import Order


class ClientListView(LoginRequiredMixin, View):
    """Class based view for Client for listing all the clients."""

    def get(self, request):
        """Render client list tempalte.."""
        clients = Client.objects.all()
        context = {
            'clients': clients,
        }
        return render(request, 'client/list-clients.html', context)


client_list_view = ClientListView.as_view()


class ClientDetailView(LoginRequiredMixin, View):
    """Class based view for displaying client detail."""

    def get(self, request, pk, format=None):
        """Get client details by id ."""
        client = get_object_or_404(Client, id=pk)
        orders = Order.objects.filter(client=client)
        measurements, measurements_exist = get_measurements(pk, client)
        context = {
            'client': client,
            'measurements': measurements,
            'measurements_exist': measurements_exist,
            'is_male': client.gender == 'M',
            'orders': orders
        }
        return render(request, 'client/client-detail.html', context)


client_detail_view = ClientDetailView.as_view()


class ClientDeleteView(LoginRequiredMixin, View):
    """Class based view for displaying client detail."""

    def post(self, request):
        """Delete client by id ."""
        pk = request.POST.get('id')
        client_to_delete = get_object_or_404(Client, id=pk)
        client_to_delete.delete()
        return redirect('client:clients')


client_delete_view = ClientDeleteView.as_view()


class ClientAddView(LoginRequiredMixin, View):
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
            return render(request, 'client/add-client.html', {'form': form, 'func': 'Add'})


client_add_view = ClientAddView.as_view()


class ClientUpdateView(LoginRequiredMixin, View):
    """Class based view for displaying client detail."""

    def get(self, request, pk):
        """Return update client form."""
        client = get_object_or_404(Client, id=pk)
        form = ClientForm(instance=client)
        return render(request, 'client/add-client.html',
                      {'form': form,
                       'func': 'Update',
                       'client': client})

    def post(self, request, pk):
        """Update client by id ."""
        client = get_object_or_404(Client, id=pk)
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client:clients')
        else:
            return render(request, 'client/add-client.html', {'form': form, 'client': client})


client_update_view = ClientUpdateView.as_view()
