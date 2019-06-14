import json
from django.shortcuts import render
from medicare_appeals.appeals.views import get_receipt_dispositions, format_dashboard_response
from medicare_appeals.appeals import schema


def dashboard(request):
    results = schema.dashboard()
    start = request.GET.get('start', '')
    end = request.GET.get('end', '')
    query_results = get_receipt_dispositions(start, end, results=results)
    output = format_dashboard_response(query_results)
    context = {'data': json.dumps(output)}
    return render(request, 'pages/dashboard.html', context=context)


def reports(request):
    results = schema.dashboard()
    start = request.GET.get('start', '')
    end = request.GET.get('end', '')
    query_results = get_receipt_dispositions(start, end, results=results)
    output = format_dashboard_response(query_results)
    context = {'data': json.dumps(output)}
    return render(request, 'pages/reports.html', context=context)
