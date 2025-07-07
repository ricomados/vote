from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .forms import RatingForm
from .models import Project, Vote


class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.annotate(avg=Avg("votes__score")).order_by("-avg")


class ProjectDetailView(View):
    template_name = "projects/project_detail.html"

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = RatingForm()
        context = {
            "project": project,
            "form": form,
            "avg": project.average_score(),
            "total": project.votes.count(),
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = RatingForm(request.POST)
        if form.is_valid():
            Vote.objects.create(project=project, score=int(form.cleaned_data["score"]))
            return redirect(reverse("projects:result", args=[project.pk]))
        context = {
            "project": project,
            "form": form,
            "avg": project.average_score(),
            "total": project.votes.count(),
        }
        return render(request, self.template_name, context)


class ResultView(View):
    template_name = "projects/result.html"

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        avg = project.average_score()
        total_votes = project.votes.count()
        return render(
            request,
            self.template_name,
            {"project": project, "avg": avg, "total": total_votes},
        )
