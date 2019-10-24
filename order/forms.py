"""Forms for order application."""

import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import SelectDateWidget

from order.models import Order, Task


class OrderForm(forms.ModelForm):
    """Order model mapped form."""

    delivery_date = forms.DateField(widget=SelectDateWidget(empty_label="Delivery Date"))

    class Meta:
        """Specify fields to include."""

        model = Order
        exclude = ('product_id', 'date_recieved', 'client_id')

    def clean_delivery_date(self):
        """Check if date is valid."""
        delivery_date = self.cleaned_data['delivery_date']

        if delivery_date < datetime.date.today():
            raise ValidationError(('Delivery date can not be in past.'))

        return delivery_date


class TaskForm(forms.ModelForm):
    """Task model mapped form."""

    deadline = forms.DateField(widget=SelectDateWidget(empty_label="Deadline"))

    class Meta:
        """Specify fields to include."""

        model = Task
        exclude = ('order_id',)

    def clean_deadline(self):
        """Check if date is valid."""
        deadline = self.cleaned_data['deadline']

        if deadline < datetime.date.today():
            raise ValidationError(('Deadline can not be in past.'))

        return deadline
