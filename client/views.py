"""All the views."""

from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Client
from .serializer import ClientSerializer
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status


class ClientView(APIView):
    """Class based view for Client for listing and adding."""

    def get(self, request):
        """Get clients view."""
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """Add new client through post request."""
        data = JSONParser().parse(request)
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


client_view = ClientView.as_view()


class ClientDetailView(APIView):
    """Class based view for Client for updating, getting and deleting."""

    def get_object(self, pk):
        """Firs we see if client exists."""
        try:
            return Client.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """Get client by id view."""
        client = self.get_object(pk=pk)
        serializer = ClientSerializer(client)
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):
        """Update client."""
        client = self.get_object(pk=pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        """Delete existing client."""
        client = self.get_object(pk=pk)
        client.delete()
        return HttpResponse(status=204)


client_detail_view = ClientDetailView.as_view()
