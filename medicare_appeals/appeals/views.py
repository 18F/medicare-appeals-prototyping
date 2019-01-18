from django.shortcuts import render
from django.conf import settings


def index(request):
    context = {"title": "Home", "message": "Welcome to Medicare Appeals"}
    return render(request, 'pages/index.html', context)
