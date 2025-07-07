from django.contrib import admin
from django.db.models import Avg

from .models import Project, Vote


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "average_score_display", "created")
    search_fields = ("title",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(avg_score=Avg("votes__score")).order_by("-avg_score")

    def average_score_display(self, obj):
        """소수 1자리까지 표시하며, 정렬 가능 컬럼."""
        return round(getattr(obj, "avg_score", 0) or 0, 1)

    average_score_display.short_description = "평균 점수"
    average_score_display.admin_order_field = "avg_score"


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("project", "score", "created")
    list_filter = ("score",)
