import json
from django.shortcuts import render
from medicare_appeals.appeals import queries
from medicare_appeals.appeals import schema


def dashboard(request):
    results = schema.dashboard()
    start = request.GET.get('start', '')
    end = request.GET.get('end', '')
    query_results = queries.get_overview(start, end, results=results)
    context = {'data': json.dumps(query_results)}
    return render(request, 'pages/dashboard.html', context=context)


def reports(request):
    results = schema.dashboard()
    start = request.GET.get('start', '')
    end = request.GET.get('end', '')
    query_results = queries.get_overview(start, end, results=results)
    context = {'data': json.dumps(query_results)}
    return render(request, 'pages/reports.html', context=context)
