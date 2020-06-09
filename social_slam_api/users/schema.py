import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery

from users.models import Skill, UserSkillLevel


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class SkillType(DjangoObjectType):
    class Meta:
        model = Skill


class UserSkillLevelType(DjangoObjectType):
    class Meta:
        model = UserSkillLevel


class UserQuery(UserQuery, MeQuery, graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_skills = graphene.List(SkillType)

    def resolve_all_users(self, info, **kwargs):
        return get_user_model().objects.all()

    def resolve_all_skills(self, info, **kwargs):
        return Skill.objects.all()







