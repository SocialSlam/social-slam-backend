import graphene
from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery

from users.models import Skill, Slammer, UserSkillLevel


class UserType(DjangoObjectType):
    class Meta:
        model = Slammer


class SkillType(DjangoObjectType):
    class Meta:
        model = Skill


class UserSkillLevelType(DjangoObjectType):
    class Meta:
        model = UserSkillLevel

class SlammerQuery(UserQuery, MeQuery, graphene.ObjectType):
    all_slammers = graphene.List(UserType)
    all_skills = graphene.List(SkillType)

    def resolve_all_slammers(self, info, **kwargs):
        return Slammer.objects.all()

    def resolve_all_skills(self, info, **kwargs):
        return Skill.objects.all()

    def resolve_skill