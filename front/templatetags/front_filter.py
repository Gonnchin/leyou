from django.template import Library

register = Library()


@register.filter
def myrange(num):
    if not num:
        return []
    return [i for i in range(num)]