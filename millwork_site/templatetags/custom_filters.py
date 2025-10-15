from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """Split a string by the given delimiter"""
    if value:
        return [item.strip() for item in value.split(arg)]
    return []

