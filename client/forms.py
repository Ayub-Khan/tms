"""Forms for Client application."""

import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from client.models import Client, FemaleMeasurements, MaleMeasurements


class ClientForm(ModelForm):
    """Client model mapped form."""

    class Meta:
        """Specify fields to include."""

        model = Client
        fields = '__all__'

    def clean_name(self):
        """Check if name is valid."""
        name = self.cleaned_data['name']

        if not self._validate_name(name):
            raise ValidationError(('Invalid name.'))

        return name

    def clean_phone_number(self):
        """Check if phone is valid."""
        phone_number = self.cleaned_data['phone_number']

        if not self._validate_phone_number(phone_number):
            raise ValidationError(('Invalid phone number.'))

        return phone_number

    def _validate_name(self, name):
        """Match valid name regex with name field."""
        return bool(re.match(
            r'^[_A-z]*((-|\s)*[_A-z])*$',
            str(name)
        ))

    def _validate_phone_number(self, phone):
        """Match valid phone number regex with phone field."""
        return bool(re.match(
            r'^[+]{1,1}[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\.0-9]{0,15}$',
            str(phone)
        ))


class MaleMeasurementsForm(ModelForm):
    """MaleMeasurements model mapped form."""

    class Meta:
        """Specify fields to include."""

        model = MaleMeasurements
        exclude = ('client',)


class FemaleMeasurementsForm(ModelForm):
    """FemaleMeasurements model mapped form."""

    class Meta:
        """Specify fields to include."""

        model = FemaleMeasurements
        exclude = ('client',)