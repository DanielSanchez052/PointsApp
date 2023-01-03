"""PointsApp URL Configuration
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import debug_toolbar

from apps.users.custom_auth.api.routers import router as userRouter
from apps.users.user.api.routers import router as profileRouter
from apps.products.admin import productAdmin


# Documentation Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Documentación de API",
        default_version='v0.1',
        description="Documentación de API para el manejo de usuarios y puntos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sanchezd0528@gmail.com"),
        license=openapi.License(name="BSD License"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # debug
    path('__debug__/', include(debug_toolbar.urls)),

    # docs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

    # admin sites
    path('admin/', admin.site.urls, name="admin"),

    # internal modules
    path('authentication/', include('apps.users.custom_auth.urls')),
    path('', include('apps.users.user.urls')),
    path('account/', include('apps.users.points.urls')),

    # ##viewsets
    path('', include(profileRouter.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
