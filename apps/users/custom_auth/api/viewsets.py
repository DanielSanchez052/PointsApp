from rest_framework import status

from rest_framework.response import Response 
from rest_framework import viewsets 

from apps.users.custom_auth.api.serializers import UserSerializer, UserListSerializer

class UserViewSet(viewsets.GenericViewSet):
    serializer_class=UserSerializer

    def get_queryset(self,username=None):
        if username is None:
            return self.serializer_class.Meta.model.objects.filter(is_active=True)
        return self.serializer_class.Meta.model.objetcts.filter(username=username, is_active=True)
    
    def list (self,request):
        user_serialize = UserListSerializer(self.get_queryset(),many=True)
        return Response(user_serialize.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        user_serialize = self.serializer_class(data=request.data)
        if user_serialize.is_valid():
            user_serialize.save()
            return Response(user_serialize.data,status=status.HTTP_200_OK)
        return Response(user_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
