from django.contrib.auth import login, logout
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status, views, permissions

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers.authentication_serializer import LoginSerializer, ChangePasswordSerializer
from .serializers.general_serializer import UserProfileSerializer
from .authentication import CsrfExemptSessionAuthentication
from apps.core.serializers import DefaultResponse
from apps.core.utils import get_request_ip
from ..models import IpLocked


response_login = {
    "202": openapi.Response(
        description="Login Success",
        schema=UserProfileSerializer
    ),
    "403": openapi.Response(
        description="locked",
        schema=DefaultResponse
    )
}


class LoginView(views.APIView):
    serializer_class = LoginSerializer
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(tags=['authentication'], request_body=serializer_class, responses=response_login)
    def post(self, request, format=None):
        ip_request = get_request_ip(request)

        if IpLocked.objects.is_locked(ip_request):
            return Response(DefaultResponse(message="you have made too many failed attempts, please try again later", status_code=403), status=status.HTTP_403_FORBIDDEN)

        serializer = LoginSerializer(data=self.request.data, context={
                                     'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        if user.attempts > settings.LIMIT_NUMBER_SESSIONS:
            user.attempts = 0
            user.save()

        login(request, user)
        return Response(UserProfileSerializer(user).data, status=status.HTTP_202_ACCEPTED)


response_logout = {
    "202": openapi.Response(
        description="logout Success",
        schema=DefaultResponse
    ),

}


class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['authentication'], responses=response_logout)
    def post(self, request):
        logout(request)
        return Response(DefaultResponse(message="loggout success",  status_code=200), status=status.HTTP_200_OK)


response_change_password = {
    "200": openapi.Response(
        description='Change Password User Sucess',
        schema=DefaultResponse,
        examples={
            "application/json": {
                "message": "change password successfull",
                "status_code": 200
            }
        },
    ),
    "400": openapi.Response(
        description='Change Password User Sucess',
        examples={
            "application/json": {
                "old_password": [
                    "This field may not be blank."
                ],
                "new_password1": [
                    "This field may not be blank."
                ],
                "new_password2": [
                    "This field may not be blank."
                ]
            }
        },
    ),
}


class ChangePasswordView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    @swagger_auto_schema(tags=['authentication'], request_body=serializer_class, responses=response_change_password)
    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(DefaultResponse(message='change password successfull', status_code=200), status=status.HTTP_200_OK)
