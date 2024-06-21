from django.shortcuts import render


def index(request):
    """The homepage for journal records"""
    return render(request, "journal_records/index.html")
