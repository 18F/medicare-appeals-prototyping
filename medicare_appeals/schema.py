from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title=
        'Medicare Appeals Sweeping Transparency and Reconciliation Prototype API',
        default_version='v0.1',
        description=
        'Medicare Appeals Sweeping Transparency and Reconciliation Prototype API documentation',
        terms_of_service='Terms of Service: TDB',
        contact=openapi.Contact(email='andrew.burnes@gsa.gov'),
        license=openapi.License(name='CC0 1.0 Universal'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)
