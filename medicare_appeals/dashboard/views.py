from django.shortcuts import render


def dashboard(request):
    context = {
        'title': 'Dashboard',
        'message': 'Welcome to Medicare Appeals dashboard'
    }
    return render(request, 'pages/dashboard.html', context)


def reports(request):
    context = {
        'title': 'Reports',
        'message': 'Welcome to Medicare Appeals reports'
    }
    return render(request, 'pages/reports.html', context)
