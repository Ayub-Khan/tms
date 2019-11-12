"""Unit tests for create dummy clients command."""

from io import StringIO

from django.core.management import call_command
from django.test import TestCase

import ddt
from tms.utils import TestDbSetUp


@ddt.ddt
class CreateDummyClientsTest(TestCase, TestDbSetUp):
    """Dummy clients creation test class."""

    @ddt.data(
        (0, 'Can not create -ive or zero number of clients.'),
        (-1, 'Can not create -ive or zero number of clients.'),
        (100, 'Dummy clients created successfully.')
    )
    @ddt.unpack
    def test_create_dummy_clients(self, total, msg):
        """Test create dummy clients command."""
        console_output = StringIO()
        call_command('create_dummy_clients', '--total={}'.format(total), stdout=console_output)
        self.assertIn(msg, console_output.getvalue())
