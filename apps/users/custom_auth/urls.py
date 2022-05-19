from django.urls import path

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.custom_auth.api.views import LoginView, LogoutView


class ExampleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get (self, request, *args, **kwargs):
        
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)


urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('test/', ExampleView.as_view(), name='tets')
    ]


