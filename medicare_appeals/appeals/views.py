import datetime
import pytz
from django.shortcuts import render
from django.conf import settings
from django.db.models import Count
from rest_framework import response, viewsets, views
from medicare_appeals.appeals import models, serializers, schema


def index(request):
    context = {'title': 'Home', 'message': 'Welcome to Medicare Appeals'}
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


class AppealViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows appeals to be viewed or edited.
    """
    queryset = models.Appeal.objects.all()
    serializer_class = serializers.AppealSerializer


class AppellantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows appellants to be viewed or edited.
    """
    queryset = models.Appellant.objects.all()
    serializer_class = serializers.AppellantSerializer


class ClaimViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows claims to be viewed or edited
    """
    queryset = models.Claim.objects.all()
    serializer_class = serializers.ClaimSerializer


class HolisticAppealViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows holistic appeals to be viewed or edited.
    """
    queryset = models.HolisticAppeal.objects.all()
    serializer_class = serializers.HolisticAppealSerializer


class LevelViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows levels to be viewed or edited
    """
    queryset = models.Level.objects.all()
    serializer_class = serializers.LevelSerializer


class ProviderViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows providers to be viewed or edited
    """
    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer


class StatusViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows statuses to be viewed or edited
    """
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer


def format_dashboard_response(results=schema.dashboard()):
    output = []

    for level, racs in results.items():
        level_number = int(level.split()[1])
        for rac, counts in racs.items():
            sub_item = {}
            sub_item['level'] = level_number
            sub_item['denial_category'] = rac
            sub_item.update(counts)
            output.append(sub_item)

    return output


def get_receipt_dispositions(start=None, end=None, results=schema.dashboard()):
    appeal_status = models.Appeal.objects.values(
        'id', 'level__level_name','status__category', 'rac').order_by(
            'id','-status__created_at'
                ).distinct('id')

    if start and end:
        try:
            s_year, s_month, s_day = start.split('-')
            e_year, e_month, e_day = end.split('-')
            start_date = datetime.datetime(int(s_year), int(s_month), int(s_day), tzinfo=pytz.UTC)
            end_date = datetime.datetime(int(e_year), int(e_month), int(e_day), tzinfo=pytz.UTC)

            appeal_status = appeal_status.filter(
                status__created_at__range=(
                    start_date,
                    end_date
                ))
        except Exception as e:
            print(f'{e}')
            pass

    for item in appeal_status:
        rac = 'rac'

        if item['rac'] == False:
            rac = 'non-rac'

        if item['status__category'] == 'Closed':
            results[item['level__level_name']][rac]['dispositions'] = results.get(
                item['level__level_name'], {}).get(rac).get('dispositions', 0) + 1
        else:
            results[item['level__level_name']][rac]['receipts'] = results.get(
                item['level__level_name'], {}).get(rac).get('receipts', 0) + 1

    return results


class OverviewView(viewsets.ViewSet):
    """
    API endpoint to query the overview aggregates
    """

    queryset = models.Appeal.objects.all()

    def list(self, request, format=None):
        """
        Return a list of overview values.
        """
        results = schema.dashboard()
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        query_results = get_receipt_dispositions(start, end, results=results)
        output = format_dashboard_response(query_results)
        return response.Response(output)
