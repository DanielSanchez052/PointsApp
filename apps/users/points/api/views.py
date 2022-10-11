
from rest_framework import generics, views, status
from rest_framework.response import Response
from apps.users.points.models.Account import Account

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema 

from apps.users.points.models.AccountTransaction import AccountTransaction
from apps.users.user.models.Profile import Profile

from .serializers.general_serializer import AccountStatusSerializer, TransactionStatusSerializer
from .serializers.account_transaction_serializer import AccountTransactionSerializer, AddPointsProfileSerializer
from apps.core.permissions import CustomModelPermissions

# Create your views here.
class GetAccountStatus(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = AccountStatusSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active = True)

class GetTransactionStatus(generics.ListAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = TransactionStatusSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active = True)
    

class AccountTransactionView(generics.ListCreateAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = AccountTransactionSerializer
    
    queryset = AccountTransaction.objects.all()

    def list(self, request, *args, **kwargs):
        profile = Profile.objects.get(auth = request.user)
        if(profile):
            self.queryset = self.queryset.filter(account__user = profile)
            return super().list(request, *args, **kwargs)
        return Response({"message":"El usuario no tiene ningun perfil"}, status = status.HTTP_200_OK)

    
class AddPointsProfile(generics.CreateAPIView):
    permission_classes = [CustomModelPermissions]
    serializer_class = AddPointsProfileSerializer
    queryset = AccountTransaction.objects.all()

    # def create(self, request, *args, **kwargs):
    #     profile = Profile.objects.get(user = request.user)
    #     if profile:
    #         addSerializer = AddPointsProfileSerializer()
    #     return super().create(request, *args, **kwargs)
   