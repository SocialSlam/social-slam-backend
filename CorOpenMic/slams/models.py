from django.db import models


class Performance(models.Model):

    skill = models.ForeignKey('users.Skill', on_delete=models.SET_NULL, null=True)
    slam = models.ForeignKey('Slam', on_delete=models.CASCADE)
    slammer = models.ForeignKey('users.Slammer', on_delete=models.CASCADE)


class Slam(models.Model):

    audience = models.ManyToManyField('users.Slammer', related_name='slams')
    slammers = models.ManyToManyField('users.Slammer', through=Performance, related_name='performances')
