from django.shortcuts import render
from django.conf import settings


def index(request):
    context = {"title": "Home", "message": "Welcome to Medicare Appeals"}
    return render(request, 'pages/index.html', context)


def handler400(request, exception):
    return render(request, 'pages/400.html', {'exception': exception})


def handler403(request, exception):
    response = render(request, 'pages/403.html', {'exception': exception})
    response.status_code = 403
    return response


def handler404(request, exception):
    response = render(request, 'pages/404.html', {})
    response.status_code = 404
    return response


def handler500(request, exception=None):
    return render(request, 'pages/500.html', {})
