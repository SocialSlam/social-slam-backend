import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType, DjangoConnectionField
from graphql_auth.schema import UserQuery, MeQuery

from users.models import Skill, UserSkillLevel


class SkillType(DjangoObjectType):
    class Meta:
        model = Skill
        filter_fields = ['id']
        interfaces = (graphene.relay.Node, )


class UserSkillLevelType(DjangoObjectType):
    class Meta:
        model = UserSkillLevel


class UserQuery(UserQuery, MeQuery, graphene.ObjectType):
    skills = DjangoConnectionField(SkillType)

    def resolve_skills(self, info, **kwargs):
        return Skill.objects.all()







