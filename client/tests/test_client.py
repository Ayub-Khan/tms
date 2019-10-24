"""Unit tests for client application's CRUD opeartions."""

from django.conf import settings
from django.test import TestCase
from rest_framework.test import APIClient

from client.forms import ClientForm, MaleMeasurementsForm
from client.models import Client
from tms.utils import TestDbSetUp


class ClientTestCase(TestCase, TestDbSetUp):
    """Unit test for Client model's CRUD functionality."""

    api_client = APIClient()

    def setUp(self):
        """Create a dummy user for the purpose of testing."""
        self.api_client = APIClient()
        self.user, self.username, self.password = self.create_user()
        self.client = self.create_client()
        self.measurements = self.create_male_measurements(self.client)

    def test_login(self):
        """Login test case."""
        path = self.get_url_for_test_against_endpoint('/accounts/login/')
        response = self.api_client.post(path, {'username': self.username, 'password': self.password})
        # should be logged in now
        self.assertEqual(response.status_code, 302)

    def test_list_clients(self):
        """ Check list of clients."""
        self.api_client.login(username=self.username, password=self.password)
        path = self.get_url_for_test_against_endpoint('/clients/')
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
        path = self.get_url_for_test_against_endpoint('/clients/add/')
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
        path = self.get_url_for_test_against_endpoint('/clients/detail/{}/'.format(self.client.id))
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
        path = self.get_url_for_test_against_endpoint('/clients/measurements/add/{}/'.format(self.client.id))
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
        path = self.get_url_for_test_against_endpoint('/clients/delete/{}/'.format(self.client.id))
        response = self.api_client.get(
            path
        )
        # check response code returned
        self.assertEqual(response.status_code, 302)
        # check response HTML content
        self.assertEqual(Client.objects.count(), 0)
        self.api_client.logout()
