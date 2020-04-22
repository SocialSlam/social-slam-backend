import graphene
import graphql_jwt
from graphene_django import DjangoObjectType

from users.models import Slammer, Skill, UserSkillLevel


class UserType(DjangoObjectType):
    class Meta:
        model = Slammer


class SkillType(DjangoObjectType):
    class Meta:
        model = Skill


class UserSkillLevelType(DjangoObjectType):
    class Meta:
        model = UserSkillLevel


class Query(graphene.ObjectType):
    all_slammers = graphene.List(UserType)
    all_skills = graphene.List(SkillType)

    def resolve_all_slammers(self, info, **kwargs):
        return Slammer.objects.all()

    def resolve_all_skills(self, info, **kwargs):
        return Skill.objects.all()


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)