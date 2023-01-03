
from rest_framework import generics, status
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from apps.users.points.models.AccountTransaction import AccountTransaction
from apps.users.user.models.Profile import Profile

from .serializers.general_serializer import AccountStatusSerializer, TransactionStatusSerializer, TransactionSourceSerializer, TransactionTypeSerializer
from .serializers.account_transaction_serializer import AccountTransactionSerializer
from .serializers.account_serializer import AccountSerializer
from apps.core.permissions import CustomModelPermissions

# Create your views here.


class GetAccountStatus(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = AccountStatusSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)


class GetTransactionStatus(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = TransactionStatusSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)


class GetTransactionSource(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = TransactionSourceSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)


class GetTransactionType(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = TransactionTypeSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)


class GetAccount(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = AccountSerializer
    queryset = serializer_class.Meta.model.objects.all()


class AccountTransactionView(generics.ListCreateAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = AccountTransactionSerializer

    queryset = AccountTransaction.objects.all().select_related(
        'transaction_type', 'transaction_source', 'status')

    def list(self, request, *args, **kwargs):
        profile = Profile.objects.get(auth=request.user)
        if (profile):
            self.queryset = self.queryset.filter(account__user=profile)
            return super().list(request, *args, **kwargs)
        return Response({"message": "El usuario no tiene ningun perfil"}, status=status.HTTP_200_OK)
