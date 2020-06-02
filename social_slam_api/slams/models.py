from django.db import models


class Performance(models.Model):

    skill = models.ForeignKey('users.Skill', on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)


class Event(models.Model):

    audience = models.ManyToManyField('users.User', related_name='slams')
    artists = models.ManyToManyField('users.User', through=Performance, related_name='performances')
    datetime = models.DateTimeField()
    name = models.TextField(max_length=128)
    description = models.TextField(max_length=512)
