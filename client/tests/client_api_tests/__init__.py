"""Tests for rest authentication.

This package includes all the unit tests for api based class authentication and crud operations.
"""

import json

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from client.forms import ClientForm, MaleMeasurementsForm
from client.models import Client, MaleMeasurements
from client.utils import get_url_for_test_against_endpoint


class WrapperTestClass:
    """Wrapper class for our TestCase class."""

    class ClientTestCase(TestCase):
        """Common test case class having methods required in both basic and token auth tests."""

        def setUp(self):
            """Create a dummy user for the purpose of testing."""
            self.username = 'test_user'
            self.password = '12345678'
            self.user, p = User.objects.get_or_create(username=self.username)
            self.user.set_password(self.password)
            self.user.save()
            self.client_email = 'jon@nightwatch.com'
            self.client_phone = '+9290078601'
            self.client = Client.objects.create(**{
                'name': 'Jon Snow',
                'age': 18,
                'gender': 'M',
                'address': 'night watch wall',
                'phone_number': self.client_phone,
                'email': self.client_email
            })
            self.client.save()

        def test_get_login_response(self):
            """Test login."""
            api_client = self.get_authenticated_api_client()
            path = get_url_for_test_against_endpoint('/api/login')
            response = api_client.post(
                path=path,
                data=json.dumps({'username': self.username, 'password': self.password}),
                content_type='application/json'
            )
            token = json.loads(response.content)['token']
            token_from_db = Token.objects.get(user_id=self.user.id)
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(token)
            self.assertEqual(token, token_from_db.key)
            token_from_db.delete()

        def test_get_clients(self):
            """Test get client api."""
            api_client = self.get_authenticated_api_client()
            path = get_url_for_test_against_endpoint('/clients/api/')
            response = api_client.get(
                path
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.content)[0]['id'], self.client.id)

        def test_get_client_by_id(self):
            """Test get client details by id api."""
            api_client = self.get_authenticated_api_client()
            path = get_url_for_test_against_endpoint('clients/api/detail/1/')
            response = api_client.get(
                path
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.content)['email'], Client.objects.filter(id=1)[0].email)

        def test_update_client_by_id(self):
            """Test update client by id api."""
            api_client = self.get_authenticated_api_client()
            path = get_url_for_test_against_endpoint('clients/api/update/1/')
            data = {
                'name': 'Jon Snow',
                'age': 18,
                'gender': 'M',
                'address': 'night watch wall',
                'phone_number': '+9290078602',
                'email': self.client_email,
            }
            api_client.put(
                path=path,
                data=json.dumps(data),
                content_type='application/json'
            )
            self.assertTrue(Client.objects.filter(phone_number='+9290078602').exists())

        def test_add_client(self):
            """Add client by id api."""
            api_client = self.get_authenticated_api_client()
            path = get_url_for_test_against_endpoint('clients/api/add/')
            data = {
                'name': 'Jon Snow',
                'age': 18,
                'gender': 'M',
                'address': 'night watch wall',
                'phone_number': '+9290078603',
                'email': 'jon.s@nightwatch.com',
            }
            api_client.post(
                path=path,
                data=json.dumps(data),
                content_type='application/json'
            )
            self.assertTrue(Client.objects.filter(email='jon.s@nightwatch.com').exists())

        def test_delete_client_by_id(self):
            """Delete client by id api."""
            api_client = self.get_authenticated_api_client()
            path = get_url_for_test_against_endpoint('clients/api/delete/{}/'.format(str(self.client.id)))
            api_client.delete(
                path=path
            )
            self.assertFalse(Client.objects.filter(id=self.client.id).exists())
