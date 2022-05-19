from django.contrib.auth import login, logout

from rest_framework.response import Response
from rest_framework import status, views, permissions

from .serializers.authentication_serializer import LoginSerializer, LoginUserSerializer
from .authentication import CsrfExemptSessionAuthentication


class LoginView(views.APIView):
    serializer_class = LoginSerializer
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(LoginUserSerializer(user).data, status=status.HTTP_202_ACCEPTED)

#Logout 
class LogoutView(views.APIView):
    
    def post(self, request):
        logout(request)
        return Response(None, status=status.HTTP_200_OK)
        