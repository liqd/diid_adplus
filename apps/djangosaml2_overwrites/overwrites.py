from allauth.account.models import EmailAddress
from django.urls import reverse
from djangosaml2.urls import urlpatterns
from djangosaml2.views import AssertionConsumerServiceView

from .urls import urlpatterns as custom_urlpatterns


def apply_custom_overwrites():
    AssertionConsumerServiceView.customize_session = customize_session
    AssertionConsumerServiceView.custom_redirect = custom_redirect
    urlpatterns.extend(custom_urlpatterns)


def customize_session(self, user, session_info):
    if not EmailAddress.objects.filter(user=user, email=user.email).exists():
        email_address = EmailAddress(user=user, email=user.email)
        email_address.save()
    if not EmailAddress.objects.filter(user=user, primary=True).exists():
        email_address = EmailAddress.objects.get(user=user, email=user.email)
        email_address.primary = True
        email_address.save()


def custom_redirect(self, user, relay_state, session_info):
    email_address = EmailAddress.objects.get(user=user, email=user.email)
    if not email_address.verified:
        signup = reverse("saml2_signup")
        if relay_state:
            signup += "?next={}".format(relay_state)
        return signup
