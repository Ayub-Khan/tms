"""All the views."""

from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from client.models import Client
from client.serializer import ClientSerializer
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status


class ClientView(APIView):
    """Class based view for Client for listing and adding."""

    def get(self, request):
        """Get clients view."""
        clients = Client.objects.all()
        serializer_obj = ClientSerializer(clients, many=True)
        return JsonResponse(serializer_obj.data, safe=False, status=200)

    def post(self, request):
        """Add new client through post request."""
        data = JSONParser().parse(request)
        serializer_obj = ClientSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return JsonResponse(serializer_obj.data, status=201)
        return JsonResponse(serializer_obj.errors, status=400)


client_view = ClientView.as_view()


class ClientDetailView(APIView):
    """Class based view for Client for updating, getting and deleting."""

    def _get_object(self, pk):
        """First we see if client exists."""
        try:
            return Client.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """Get client by id view."""
        client = self._get_object(pk=pk)
        serializer_obj = ClientSerializer(client)
        return JsonResponse(serializer_obj.data, status=200)

    def put(self, request, pk, format=None):
        """Update client."""
        client = self._get_object(pk=pk)
        serializer_obj = ClientSerializer(client, data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return JsonResponse(serializer_obj.data, status=200)
        return JsonResponse(serializer_obj.errors, status=400)

    def delete(self, request, pk, format=None):
        """Delete existing client."""
        client = self._get_object(pk=pk)
        client.delete()
        return HttpResponse(status=204)


client_detail_view = ClientDetailView.as_view()
