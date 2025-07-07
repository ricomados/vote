from django.contrib import admin

from .models import Project, Vote


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "average_score", "created")
    search_fields = ("title",)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("project", "score", "created")
    list_filter = ("score",)
