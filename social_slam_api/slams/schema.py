import graphene
from django_filters import FilterSet
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from slams.models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        filter_fields = ['artists__id', 'audience__id', 'id', 'datetime']
        interfaces = (graphene.relay.Node, )


class EventQuery(graphene.ObjectType):
    events = DjangoFilterConnectionField(EventType)

    def resolve_events(self, info, **kwargs):
        return Event.objects.all()


class CreateEventMutation(graphene.Mutation):
    class Arguments:
        artists = graphene.List(graphene.ID)
        audience = graphene.List(graphene.ID)
        datetime = graphene.DateTime()
        title = graphene.String()

    event = graphene.Field(EventType)

    def mutate(self, info, **kwargs):
        event = Event.objects.create(datetime=kwargs.get('datetime', None),
                                     title=kwargs.get('title', None))
        event.artists.set(kwargs.get('artists', None))
        event.audience.set(kwargs.get('audience', None))
        return CreateEventMutation(event=event)