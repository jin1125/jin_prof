from django.contrib import admin

from prof.models import CareersList
from prof.models import Profile
from prof.models import Skills
from prof.models import Study


class CareersListInline(admin.TabularInline):
    model = CareersList
    extra = 1


class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 1


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('CAREERS TEXT', {'fields': ['careers_text']}),
        ('HOBBIES', {'fields': ['hobbies']}),
    ]
    inlines = [
        CareersListInline,
        SkillsInline
    ]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Study)
