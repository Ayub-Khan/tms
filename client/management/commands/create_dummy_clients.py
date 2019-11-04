"""Create dummy clients for testing purpose."""

from django.core.management.base import BaseCommand

from client.models import Client
from tms.utils import RandomDataGenerator


class Command(BaseCommand, RandomDataGenerator):
    """Create dummy clients command class."""

    help = "Create dummy clients for testing purposes."

    def add_arguments(self, parser):
        """Argument specifying how many dummy clients to create."""
        parser.add_argument(
            '--total', type=int, help='Indicates the number of clients to be created.', default=15,
        )

    def handle(self, *args, **kwargs):
        """Create 'total' dummy clients in database."""
        no_of_clients = kwargs['total']
        if no_of_clients < 1:
            self.stdout.write('Can not create -ive or zero number of clients.')

        else:
            existing_emails = Client.objects.all().values_list('email', flat=True)
            existing_phones = Client.objects.all().values_list('phone_number', flat=True)

            name_set = self.get_n_unique_names(no_of_clients)
            email_set = self.get_n_unique_emails(n=no_of_clients, existing_emails=existing_emails)
            phone_set = self.get_n_unique_numbers(n=no_of_clients, existing_phones=existing_phones)

            client_list = []

            for i in range(no_of_clients):
                client = Client(**{
                    'name': name_set[i],
                    'age': 30,
                    'gender': 'M',
                    'phone_number': phone_set[i],
                    'email': email_set[i],
                    'address': self.get_random_address(length=15)
                })
                client_list.append(client)

            Client.objects.bulk_create(client_list)
            self.stdout.write('Dummy clients created successfully.')
