from django.contrib.auth import login, logout
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status, views, permissions

from .serializers.authentication_serializer import LoginSerializer, LoginUserSerializer
from .authentication import CsrfExemptSessionAuthentication
from apps.core.utils import get_request_ip
from ..models import IpLocked

class LoginView(views.APIView):
    serializer_class = LoginSerializer
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        ip_request = get_request_ip(request)

        if IpLocked.objects.is_locked(ip_request):
            return Response({"message":"you have made too many failed attempts, please try again later"},status=status.HTTP_403_FORBIDDEN)
        
        serializer = LoginSerializer(data=self.request.data,context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        if user.attempts > 0:
            user.attempts = 0
            user.save()

        login(request, user)
        return Response(LoginUserSerializer(user).data, status=status.HTTP_202_ACCEPTED)


#Logout 
class LogoutView(views.APIView):
    
    def post(self, request):
        logout(request)
        return Response(None, status=status.HTTP_200_OK)
        