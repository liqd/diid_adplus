import factory
from allauth.account.models import EmailAddress

from adhocracy4.test import factories as a4_factories
from apps.newsletters import models


class NewsletterFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Newsletter

    sender = factory.Faker('email')
    sender_name = factory.Faker('name')
    subject = factory.Faker('sentence', nb_words=4)
    body = factory.Faker('text')

    receivers = models.PROJECT

    creator = factory.SubFactory(a4_factories.USER_FACTORY)
    project = factory.SubFactory(a4_factories.ProjectFactory)


class EmailAddressFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = EmailAddress
        django_get_or_create = ('user', 'email')
