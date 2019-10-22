"""Basic authentication based test cases."""

import json

from rest_framework.test import APIClient

from client.tests.client_api_tests import WrapperTestClass
from client.utils import get_url_for_test_against_endpoint


class TokenAuthTests(WrapperTestClass.ClientTestCase):
    """Token auth based client tests."""

    def get_authenticated_api_client(self):
        """Get token recieved on login."""
        api_client = APIClient()
        login_path = get_url_for_test_against_endpoint('/api/login')
        login_response = api_client.post(
            path=login_path,
            data=json.dumps({'username': self.username, 'password': self.password}),
            content_type='application/json'
        )
        token = json.loads(login_response.content)['token']
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        return api_client
