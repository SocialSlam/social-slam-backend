import graphene
from django.http import HttpResponse
from graphene_django import DjangoObjectType
from slams.models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class EventQuery(graphene.ObjectType):
    user_events = graphene.List(EventType)

    def resolve_user_events(self, info, **kwargs):
        if 'id' not in kwargs:
            return HttpResponse(status=400,
                                content='Please provide a valid User ID',
                                content_type='text/html')
        return Event.objects.filter(artists__id=kwargs['id']) | Event.objects.filter(audience__id=kwargs['id'])


