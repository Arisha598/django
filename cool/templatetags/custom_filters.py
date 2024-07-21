from django import template

register = template.Library()

@register.filter(name='upper_case')
def upper_case(value):
    """
    Converts the string to uppercase.
    Usage: {{ some_variable|upper_case }}
    """
    return value.upper()

@register.filter(name='reverse_string')
def reverse_string(value):
    """
    Reverses the characters in the string.
    Usage: {{ some_variable|reverse_string }}
    """
    return value[::-1]


