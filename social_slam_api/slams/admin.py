from django.contrib import admin

# Register your models here.
from users.models import Slammer, Skill, UserSkillLevel

admin.site.register(Slammer)
admin.site.register(Skill)
admin.site.register(UserSkillLevel)
