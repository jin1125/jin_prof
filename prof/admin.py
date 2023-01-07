from django.contrib import admin

from .models import CareersList
from .models import Profile
from .models import Skills


class CareersListInline(admin.TabularInline):
    model = CareersList
    extra = 1


class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 1


class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        CareersListInline,
        SkillsInline
    ]


admin.site.register(Profile, ProfileAdmin)
