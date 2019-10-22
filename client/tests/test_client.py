"""Unit tests for client application's CRUD opeartions."""

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from client.forms import ClientForm, MaleMeasurementsForm
from client.models import Client, MaleMeasurements
from client.utils import get_url_for_test_against_endpoint


class ClientTestCase(TestCase):
    """Unit test for Client model's CRUD functionality."""

    api_client = APIClient()

    def setUp(self):
        """Create a dummy user for the purpose of testing."""
        self.username = 'test_user'
        self.password = '12345'
        user, p = User.objects.get_or_create(username='test_user')
        user.set_password(self.password)
        user.save()
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

    def test_login(self):
        """Login test case."""
        path = get_url_for_test_against_endpoint('/accounts/login/')
        response = self.api_client.post(path, {'username': self.username, 'password': self.password})
        # should be logged in now
        self.assertEqual(response.status_code, 302)

    def test_list_clients(self):
        """ Check list of clients."""
        self.api_client.login(username=self.username, password=self.password)
        path = get_url_for_test_against_endpoint('/clients/')
        response = self.api_client.get(
            path
        )
        # check template used
        self.assertTemplateUsed(response, 'client/list-clients.html')
        # check response code returned
        self.assertEqual(response.status_code, 200)
        self.api_client.logout()

    def test_add_client(self):
        """Check add client template."""
        self.api_client.login(username=self.username, password=self.password)
        path = get_url_for_test_against_endpoint('/clients/add/')
        response = self.api_client.get(
            path
        )
        form = response.context['form']
        # check template used
        self.assertTemplateUsed(response, 'client/add-client.html')
        # check response code returned
        self.assertEqual(response.status_code, 200)
        # check form used in template
        self.assertIsInstance(form, ClientForm)
        self.api_client.logout()

    def test_details_client(self):
        """Detail of client and measurements."""
        self.api_client.login(username=self.username, password=self.password)
        path = get_url_for_test_against_endpoint('/clients/detail/{}/'.format(self.client.id))
        response = self.api_client.get(
            path
        )
        # check template used
        self.assertTemplateUsed(response, 'client/client-detail.html')
        # check response code returned
        self.assertEqual(response.status_code, 200)
        self.api_client.logout()

    def test_add_measurement(self):
        """Get add view of measurement."""
        self.api_client.login(username=self.username, password=self.password)
        path = get_url_for_test_against_endpoint('/clients/measurements/add/{}/'.format(self.client.id))
        response = self.api_client.get(
            path
        )
        form = response.context['form']
        # check template used
        self.assertTemplateUsed(response, 'client/add-measurements.html')
        # check response code returned
        self.assertEqual(response.status_code, 200)
        # check form used in template
        self.assertIsInstance(form(), MaleMeasurementsForm)
        self.api_client.logout()

    def test_delete_clients(self):
        """Delete client."""
        self.api_client.login(username=self.username, password=self.password)
        path = get_url_for_test_against_endpoint('/clients/delete/{}/'.format(self.client.id))
        response = self.api_client.get(
            path
        )
        # check response code returned
        self.assertEqual(response.status_code, 302)
        # check response HTML content
        self.assertEqual(Client.objects.count(), 0)
        self.api_client.logout()
