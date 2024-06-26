"""Define URL patterns for journal_records"""

from django.urls import path

from . import views

app_name = "journal_records"
urlpatterns = [
    path("", views.index, name="index"),
    path("topics/", views.topics, name="topics"),
    path("topics/<int:topic_id>/", views.topic, name="topic"),
]