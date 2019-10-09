"""All the views."""

from django.shortcuts import redirect, render, get_object_or_404
from tailor_management_system.forms import ClientForm
from .models import Client
from django.views.generic import ListView, DetailView

# Create your views here.


class IndexView(ListView):
    """Index view."""

    template_name = 'tailor_management_system/index.html'
    context_object_name = 'client_list'

    def get_queryset(self):
        """Get all clients."""
        return Client.objects.all()


index_view = IndexView.as_view()


class ClientDetailView(DetailView):
    """Detail view."""

    model = Client
    template_name = 'tailor_management_system/client-detail.html'


client_detail_view = ClientDetailView.as_view()


def clientView(request):
    """Add new client."""
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = ClientForm()
    return render(
        request,
        'tailor_management_system/client.html',
        {'form': form}
        )


def edit(request, pk, template_name='tailor_management_system/edit.html'):
    """Edit client."""
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form})


def delete(
    request,
    pk,
    template_name='tailor_management_system/confirm_delete.html'
):
    """Delete client."""
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('index')
    return render(request, template_name, {'object': client})
