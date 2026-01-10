from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/reporter/", views.reporter_dashboard, name="reporter-dashboard"),
    path("articles/new/", views.article_create, name="article-create"),
    path("articles/<int:pk>/edit/", views.article_edit, name="article-edit"),
]
