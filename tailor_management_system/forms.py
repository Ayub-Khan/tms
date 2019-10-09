"""Form for Client."""

from django import forms
from client.models import Client


class ClientForm(forms.ModelForm):
    """Form for model client."""

    class Meta:
        """Meta nested class."""

        model = Client
        fields = "__all__"
