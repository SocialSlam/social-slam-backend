from django.db import models


class Performance(models.Model):

    skill = models.ForeignKey('users.Skill', on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey('Slam', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)


class Event(models.Model):

    audience = models.ManyToManyField('users.User', related_name='slams')
    participants = models.ManyToManyField('users.User', through=Performance, related_name='performances')
    datetime = models.DateTimeField()
    name = models.TextField(max_length=128)
    description = models.TextField(max_length=512)
