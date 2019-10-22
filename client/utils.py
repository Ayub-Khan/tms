"""Utility class for frequently needed functions."""

from urllib.parse import urlunparse

from django.core.exceptions import ObjectDoesNotExist

from client.models import FemaleMeasurements, MaleMeasurements


def get_measurements(client_id, client):
    """Get measurements against a client."""
    try:
        if client.gender == 'M':
            return MaleMeasurements.objects.get(client=client_id), True
        else:
            return FemaleMeasurements.objects.get(client=client_id), True
    except ObjectDoesNotExist:
        return None, False


def get_url_for_test_against_endpoint(endpoint):
    """Return complete URL against end point for test cases."""
    return urlunparse(('http', '127.0.0.1:8000', endpoint, None, None, None))
