import datetime
import json
from django.shortcuts import render
from medicare_appeals.appeals import queries
from medicare_appeals.appeals import schema


def dashboard(request):
    today = datetime.date.today().strftime('%Y-%m-%d')
    results = schema.dashboard()
    start = request.GET.get('start', '2012-04-01')
    end = request.GET.get('end', today)
    query_results = queries.get_overview(start, end, results=results)
    context = {'data': json.dumps(query_results)}
    return render(request, 'pages/dashboard.html', context=context)


def reports(request):
    today = datetime.date.today().strftime('%Y-%m-%d')
    results = schema.dashboard()
    start = request.GET.get('start', '2012-04-01')
    end = request.GET.get('end', today)
    query_results = queries.get_overview(start, end, results=results)
    context = {'data': json.dumps(query_results)}
    return render(request, 'pages/reports.html', context=context)
