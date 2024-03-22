from django import template

register = template.Library()

@register.filter(name='to_str')
def int_to_str(value):
    return str(value)