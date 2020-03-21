from django.db import models


class Performance(models.Model):

    skill = models.ForeignKey('users.Skill')


class Slam(models.Model):

    audience = models.ManyToManyField('users.SlamUser')
    slammers = models.ManyToManyField('users.SlamUser', through=Performance)
