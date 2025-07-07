from django.urls import path

from .views import ProjectListView, ProjectDetailView, ResultView

app_name = "projects"

urlpatterns = [
    path("", ProjectListView.as_view(), name="list"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="detail"),
    path("<int:pk>/result/", ResultView.as_view(), name="result"),
] 