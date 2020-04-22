import graphene
from graphene_django import DjangoObjectType

from users.models import Slammer


class UserType(DjangoObjectType):
    class Meta:
        model = Slammer


class Query(graphene.ObjectType):
    all_slammers = graphene.List(UserType)

    def resolve_all_slammers(self, info, **kwargs):
        return Slammer.objects.all()


schema = graphene.Schema(query=Query)
