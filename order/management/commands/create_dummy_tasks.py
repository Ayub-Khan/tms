"""Create dummy employees for testing purpose."""

from django.core.management.base import BaseCommand, CommandError

from order.models import Order, Task
from tms.constants import DUMMY_ORDER_MARKER, DUMMY_TASK_MARKER
from tms.utils import RandomDataGenerator, get_future_date


class Command(BaseCommand, RandomDataGenerator):
    """Create dummy orders class."""

    help = "Create dummy orders for testing purposes."

    def add_arguments(self, parser):
        """Argument specifying how many dummy employees to create."""
        parser.add_argument(
            '--total', type=int, help='Indicates the number of clients to be created.', default=15,
        )

    def handle(self, *args, **kwargs):
        """Create 'total' dummy tasks in database."""
        no_of_tasks = kwargs['total']
        orders = Order.objects.filter(order=DUMMY_ORDER_MARKER)

        if (no_of_tasks < 1) or (orders.count() == 0):
            self.stdout.write("Can not create -ive or zero number of tasks against 0 or no orders.")

        else:
            no_of_orders = self.get_random_number(lower_limit=1, upper_limit=no_of_tasks)
            chosen_orders = []
            for i in range(0, no_of_orders):
                chosen_orders.append(orders[self.get_random_number(upper_limit=orders.count())])

            tasks = []
            for i in range(0, no_of_tasks):
                task = Task(
                    **{
                        'order': chosen_orders[self.get_random_number(upper_limit=len(chosen_orders))],
                        'status': Task.CREATED,
                        'description': DUMMY_TASK_MARKER,
                        'deadline': get_future_date(5)
                    }
                )
                tasks.append(task)

            Task.objects.bulk_create(tasks)
            self.stdout.write("Dummy tasks created successfully.")
