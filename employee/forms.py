"""Forms for employee application."""

import datetime

from django import forms
from django.core.exceptions import ValidationError

from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    """Order model mapped form."""

    class Meta:
        """Specifying fields to include."""

        model = Employee
        exclude = ('joining_date',)
