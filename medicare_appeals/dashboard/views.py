from django.shortcuts import render

def dashboard(request):
    context = {'title': 'Dashboard', 'message': 'Welcome to Medicare Appeals dashboard'}
    return render(request, 'pages/dashboard.html', context)
