from django import template
from django.contrib.auth import get_user_model

register = template.Library()
UserModel = get_user_model()
@register.filter
def placeholder(field, token):
    field.field.widget.attrs['placeholder'] = token
    return field

@register.filter
def get_guitar(user):
    print(user.guitar)
    return user.guitar


