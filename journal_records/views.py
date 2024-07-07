from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm


def index(request):
    """The homepage for journal records"""
    return render(request, "journal_records/index.html")


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "journal_records/topics.html", context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "journal_records/topic.html", context)


def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process the data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("journal_records:topics")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "journal_records/new_topic.html", context)


def new_entry(request, topic_id):
    """Add a new entry for a specific topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.save()
            return redirect("journal_records:topic", topic_id=topic_id)

    # Display a blank or invalid form.
    context = {"topic": topic, "form": form}
    return render(request, "journal_records/new_entry.html", context)
