from django.shortcuts import render

from .models import Topic


def index(request):
    """The homepage for journal records"""
    return render(request, "journal_records/index.html")


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "journal_records/topics.html", context)
