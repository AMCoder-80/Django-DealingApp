from django.template import Library

register = Library()


@register.filter()
def placeholder(value, token):
    value.field.widget.attrs['placeholder'] = token
    return value
