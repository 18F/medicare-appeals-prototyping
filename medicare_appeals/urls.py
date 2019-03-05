from django.contrib import admin
from django.conf import settings
from django.urls import include, path, re_path
from rest_framework import permissions, routers
from medicare_appeals.appeals import views
from medicare_appeals.dashboard.views import dashboard
from medicare_appeals.schema import schema_view

handler400 = 'medicare_appeals.appeals.views.handler400'
handler403 = 'medicare_appeals.appeals.views.handler403'
handler404 = 'medicare_appeals.appeals.views.handler404'
handler500 = 'medicare_appeals.appeals.views.handler500'

router = routers.DefaultRouter()
router.register(r'appeals', views.AppealViewSet)
router.register(r'appellants', views.AppellantViewSet)
router.register(r'claims', views.ClaimViewset)
router.register(r'holistic_appeals', views.HolisticAppealViewSet)
router.register(r'levels', views.LevelViewset)
router.register(r'providers', views.ProviderViewset)
router.register(r'statuses', views.StatusViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('dashboard/', dashboard),
    path('api/', include(router.urls)),
    re_path(
        r'^docs(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    re_path(
        r'^docs/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    re_path(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
