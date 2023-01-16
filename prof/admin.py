"""profアプリケーションの管理サイト設定ファイル"""
from django.contrib import admin

from prof.models import CareersList
from prof.models import Comments
from prof.models import Profile
from prof.models import Skills
from prof.models import Study


class CareersListInline(admin.TabularInline):
    """ProfileでのCareersListモデルのインライン表示設定"""
    model = CareersList
    extra = 1


class SkillsInline(admin.TabularInline):
    """ProfileでのSkillsモデルのインライン表示設定"""
    model = Skills
    extra = 1


class ProfileAdmin(admin.ModelAdmin):
    """管理サイトでのProfileモデル表示設定"""
    fieldsets = [
        ('HOME ADDRESS', {'fields': ['home_address']}),
        ('CAREERS TEXT', {'fields': ['careers_text']}),
        ('HOBBIES', {'fields': ['hobbies']}),
    ]
    inlines = [
        CareersListInline,
        SkillsInline
    ]


class CommentsInline(admin.TabularInline):
    """StudyでのCommentsモデルのインライン表示設定"""
    model = Comments
    extra = 1


class StudyAdmin(admin.ModelAdmin):
    """管理サイトでのStudyモデル表示設定"""
    fieldsets = [
        ('TITLE', {'fields': ['title']}),
        ('URL', {'fields': ['url']}),
    ]
    inlines = [
        CommentsInline
    ]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Study, StudyAdmin)
