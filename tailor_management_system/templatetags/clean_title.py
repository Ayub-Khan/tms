"""Title cleaning custom tag."""

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.simple_tag
def clean_title(title):
    """Convert string to title case."""
    return title.replace('_', ' ').title()
