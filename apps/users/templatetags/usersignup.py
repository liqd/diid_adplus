from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def usersignup():
    return getattr(settings, "USER_REGISTRATION", "")
