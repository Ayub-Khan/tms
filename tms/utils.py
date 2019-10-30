"""Utility class for frequently needed functions."""

import os
from datetime import datetime, timedelta
from urllib.parse import urlunparse

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient

from client.models import Client, MaleMeasurements
from employee.models import Employee
from order.models import Order, Task
from product.models import Product, ProductImages


class TestDbSetUp:
    """Functions needed to set Database for tests."""

    def create_user(self):
        """Create a user."""
        username = 'test_user'
        password = '12345'
        user, p = User.objects.get_or_create(username=username)
        user.set_password(password)
        user.save()
        return user, username, password

    def create_client(self):
        """Create a Client."""
        client = Client.objects.create(**{
            'name': 'Jon Snow',
            'age': 18,
            'gender': 'M',
            'address': 'night watch wall',
            'phone_number': '+9290078601',
            'email': 'jon@nightwatch.com'
        })
        client.save()
        return client

    def create_order(self, client):
        """Create an order."""
        delivery_date = datetime.today() + timedelta(days=5)
        order = Order.objects.create(**{
            'client': client,
            'status': 'I',
            'payment_status': False,
            'payment_amount': 1500,
            'advance_payment_amount': 500,
            'delivery_date': delivery_date.strftime('%Y-%m-%d'),
            'order': 'Shalwar Kameez',
            'instructions': 'Ban instead of collar.'
        })
        order.save()
        return order

    def create_employee(self):
        """Create employee."""
        employee = Employee.objects.create(**{
            'name': 'Jon Snow',
            'gender': 'M',
            'address': 'night watch wall',
            'phone_number': '+9290078601',
        })
        employee.save()
        return employee

    def create_product(self):
        """Create product."""
        product = Product.objects.create(**{
            'title': 'S Afr',
            'product_type': 'Shalwar Kameez',
            'stock': 200,
            'price': 5000,
        })
        product.save()
        return product

    def create_product_images(self, product):
        """Create product."""
        path = pth = settings.BASE_DIR + '/tms/test_image.jpg'
        test_img = SimpleUploadedFile(
            name='test_image.jpg',
            content=open(path, 'rb').read(),
            content_type='image/jpeg'
        )
        product_images = ProductImages.objects.create(**{
            'product': product,
            'image1': test_img
        })
        product_images.save()
        return product_images

    def create_task(self, order, employee):
        """Create task."""
        delivery_date = datetime.today() + timedelta(days=5)
        task = Task.objects.create(**{
            'order': order,
            'employee': employee,
            'status': 'I',
            'description': 'Stitch the shirt.',
            'deadline': delivery_date.strftime('%Y-%m-%d'),
        })
        task.save()
        return task

    def create_male_measurements(self, client):
        """Create male measurement model."""
        measurements = MaleMeasurements.objects.create(**{
            'client': client,
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
        measurements.save()
        return measurements
