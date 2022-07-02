"""PointsApp URL Configuration
"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import debug_toolbar

from apps.users.custom_auth.api.routers import router as userRouter 

from apps.users.user.api.routers import router as profileRouter


# Documentation Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Documentación de API",
        default_version='v0.1',
        description="Documentación pública de API de para matriculas y manejo de estudiantes, profesores y cursos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sanchezd0528@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    ##debug
    path('__debug__/', include(debug_toolbar.urls)),
    
    ##docs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    
    ##internal modules
    path('auth/', include('apps.users.custom_auth.urls')),
    path('', include('apps.users.user.urls')),

    # ##viewsets
    path('',include(profileRouter.urls))
    
]
