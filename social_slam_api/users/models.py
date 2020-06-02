from django.contrib.auth.models import AbstractUser
from django.db import models


class Skill(models.Model):

    skill_category_choices = [
        (0, 'Music'),
        (1, 'Dance'),
        (2, 'Poetry'),
        (3, 'Art'),
        (4, 'Fitness'),
        (5, 'Pitch'),
    ]

    skill_category = models.SmallIntegerField(choices=skill_category_choices)


class UserSkillLevel(models.Model):

    skill_level_choices = [
        (0, 'Beginner'),
        (1, 'Novice'),
        (2, 'Intermediate'),
        (3, 'Expert'),
        (4, 'Professional'),
    ]

    skill_level = models.SmallIntegerField(choices=skill_level_choices)
    user = models.ForeignKey('Slammer', on_delete=models.CASCADE, related_name='user_skill_levels')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='user_skill_levels')


class User(AbstractUser):

    skills = models.ManyToManyField(Skill, through=UserSkillLevel)
