from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from medicare_appeals.appeals import models, serializers


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
