"""Tests for order application."""

from urllib.parse import urlunparse

from django.test import TestCase
from rest_framework.test import APIClient

from order.forms import TaskForm
from tms.utils import TestDbSetUp


class TaskTestCase(TestCase, TestDbSetUp):
    """Unit tests for order operations."""

    def setUp(self):
        """Set up client, user and order for tests."""
        self.api_client = APIClient()
        self.user, self.username, self.password = self.create_user()
        self.client = self.create_client()
        self.order = self.create_order(self.client)
        self.employee = self.create_employee()
        self.task = self.create_task(self.order, self.employee)

    def test_get_tasks_list(self):
        """Get tasks list test case."""
        self.api_client.login(username=self.username, password=self.password)
        path = self.get_url_for_test_against_endpoint('/tasks/')
        response = self.api_client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task/list-tasks.html')
        self.api_client.logout()

    def test_get_task(self):
        """Get task test case."""
        self.api_client.login(username=self.username, password=self.password)
        path = self.get_url_for_test_against_endpoint('/task/1/')
        response = self.api_client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task/task-detail.html')
        self.api_client.logout()

    def test_add_task(self):
        """Check add task template."""
        self.api_client.login(username=self.username, password=self.password)
        path = self.get_url_for_test_against_endpoint('/task/add/{}/'.format(self.order.id))
        response = self.api_client.get(
            path
        )
        form = response.context['form']
        self.assertTemplateUsed(response, 'task/add-task.html')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(form, TaskForm)
        self.api_client.logout()

    def test_delete_task(self):
        """Delete task test case."""
        self.api_client.login(username=self.username, password=self.password)
        path = self.get_url_for_test_against_endpoint('/task/delete/1/')
        response = self.api_client.get(path)
        self.assertEqual(response.status_code, 200)
        self.api_client.logout()
