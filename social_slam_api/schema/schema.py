import graphene
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations
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


class Query(UserQuery, MeQuery, graphene.ObjectType):
    all_slammers = graphene.List(UserType)
    all_skills = graphene.List(SkillType)

    def resolve_all_slammers(self, info, **kwargs):
        return Slammer.objects.all()

    def resolve_all_skills(self, info, **kwargs):
        return Skill.objects.all()


class Mutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
