from django import template

register = template.Library()

@register.filter
def reverse_string(value):
    return value[::-1]

@register.filter
def multiply(value, arg):
    return value * arg