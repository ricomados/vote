from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg


class Project(models.Model):
    """프로젝트(과제) 정보 저장"""

    title = models.CharField("제목", max_length=200)
    description = models.TextField("상세 내용")

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def average_score(self) -> float:
        """평균 점수(소수 1자리)를 계산하여 반환"""
        avg = self.votes.aggregate(avg=Avg("score"))["avg"]
        return round(avg or 0, 1)


class Vote(models.Model):
    """프로젝트 평가 점수 저장 (1~5점)"""

    project = models.ForeignKey(
        Project, related_name="votes", on_delete=models.CASCADE
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="점수 (1~5)",
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "평가"
        verbose_name_plural = "평가들"

    def __str__(self):
        return f"{self.project.title}: {self.score}점"
