"""Unit tests for client application's CRUD opeartions."""

from django.conf import settings
from django.test import TestCase
from rest_framework.test import APIClient

from client.forms import ClientForm, MaleMeasurementsForm
from client.models import Client, MaleMeasurements


class ClientTestCase(TestCase):
    """Unit test for Client model's CRUD functionality."""

    api_client = APIClient()

    def setUp(self):
        """Create a dummy user for the purpose of testing."""
        self.api_url = settings.BASE_URL + '/clients/'
        self.client = Client.objects.create(**{
            'name': 'Jon Snow',
            'age': 18,
            'gender': 'M',
            'address': 'night watch wall',
            'phone_number': '+9290078601',
            'email': 'jon@nightwatch.com'
        })
        self.client.save()
        self.measurements = MaleMeasurements.objects.create(**{
            'client': self.client,
            'unit': 'cm',
            'shoulder': 12,
            'armscye': 12,
            'chest': 12,
            'bust': 12,
            'waist': 12,
            'arm_length': 12,
            'hips': 12,
            'ankle': 12,
            'neck': 12,
            'back_width': 12,
            'inseam': 12,
            'wrist': 12,
            'crutch_depth': 12,
            'waist_to_knee': 12,
            'knee_line': 12,
            'biceps': 12,

        })
        self.measurements.save()

    def test_list_clients(self):
        """Check list of clients."""
        response = self.api_client.get(
            self.api_url
        )
        # check template used
        self.assertTemplateUsed(response, 'client/list-clients.html')
        # check response code returned
        self.assertEqual(response.status_code, 200)

    def test_add_client(self):
        """Check add client template."""
        response = self.api_client.get(
            self.api_url+'add/'
        )
        form = response.context['form']
        # check template used
        self.assertTemplateUsed(response, 'client/add-client.html')
        # check response code returned
        self.assertEqual(response.status_code, 200)
        # check form used in template
        self.assertIsInstance(form, ClientForm)

    def test_details_client(self):
        """Detail of client and measurements."""
        response = self.api_client.get(
            self.api_url+'detail/'+str(self.client.id)+'/'
        )
        # check template used
        self.assertTemplateUsed(response, 'client/client-detail.html')
        # check response code returned
        self.assertEqual(response.status_code, 200)

    def test_add_measurement(self):
        """Get add view of measurement."""
        response = self.api_client.get(
            self.api_url+'measurements/add/'+str(self.client.id)+'/'
        )
        form = response.context['form']
        # check template used
        self.assertTemplateUsed(response, 'client/add-measurements.html')
        # check response code returned
        self.assertEqual(response.status_code, 200)
        # check form used in template
        self.assertIsInstance(form(), MaleMeasurementsForm)

    def test_delete_clients(self):
        """Delete client."""
        response = self.api_client.get(
            self.api_url+'delete/'+str(self.client.id)+'/'
        )
        # check response code returned
        self.assertEqual(response.status_code, 302)
        # check response HTML content
        self.assertEqual(Client.objects.count(), 0)
