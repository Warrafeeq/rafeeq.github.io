from django import template

register = template.Library()

@register.filter
def split(value, delimiter=','):
    """Split a string by delimiter"""
    if value:
        return value.split(delimiter)
    return []

@register.filter
def trim(value):
    """Trim whitespace from string"""
    if value:
        return value.strip()
    return value