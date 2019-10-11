"""Unit tests for client application's CRUD opeartions."""

from django.test import TestCase
from rest_framework.test import APIClient
from client.models import Client
import json
from django.conf import settings


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

    def test_get_clients(self):
        """Test get all clients."""
        """Get all(one at the moment) clients &
        see if it's id matches with id of client retrieved
        in response."""
        response = self.api_client.get(
            self.api_url
        )
        self.assertEqual(json.loads(response.content)[0]['id'], self.client.id)

    def test_add_client(self):
        """Add new client and check if it's added in all_objects list."""
        response = self.api_client.post(
            path=self.api_url,
            data=json.dumps({
                'name': 'Jon Snow',
                'age': 18,
                'gender': 'M',
                'address': 'night watch wall',
                'phone_number': '+9290078602',
                'email': 'jon.s@nightwatch.com',
            }),
            content_type='application/json'
        )
        self.assertTrue(Client.objects.filter(id=2).exists())

    def test_update_clien_by_id(self):
        """Test update fucntionality."""
        """Update existing client's email & retrieve later
        and compare with new email."""
        response = self.api_client.put(
            path=self.api_url + '1/',
            data=json.dumps({
                'name': 'Jon Snow',
                'age': 18,
                'gender': 'M',
                'address': 'night watch wall',
                'phone_number': '+9290078603',
                'email': 'jon.sn@nightwatch.com',
            }),
            content_type='application/json'
        )
        self.assertEqual(
            Client.objects.filter(
                email='jon.sn@nightwatch.com'
            ).exists(),
            True
        )

    def test_get_client_by_id(self):
        """Test retrieve by id."""
        """Get client by ID and see if a client exists
         against that id in database."""
        response = self.api_client.get(
            path=self.api_url + '1/'
        )
        self.assertEqual(
            json.loads(response.content)['email'],
            Client.objects.filter(id=1)[0].email
        )

    def test_delete_client_by_id(self):
        """Test delete by id."""
        """Delete client by id and make sure no client
        exists against that id after deletion."""
        response = self.api_client.delete(
            path=self.api_url + '1/'
        )
        self.assertFalse(Client.objects.filter(id=1).exists())
