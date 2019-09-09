from django import template

register = template.Library()


@register.filter
def is_empty(list):
    return bool(len(list))
