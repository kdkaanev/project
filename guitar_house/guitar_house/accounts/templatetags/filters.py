from django import template
from django.contrib.auth import get_user_model
from django.db.models import Avg

register = template.Library()
UserModel = get_user_model()
@register.filter
def placeholder(field, token):
    field.field.widget.attrs['placeholder'] = token
    return field

@register.filter
def get_guitar(user):
    return user.guitar

@register.filter
def average_rating(guitar):
    avg_rating = guitar.review_set.aggregate(Avg('rating'))
    avg_rating = avg_rating['rating__avg']
    return avg_rating



