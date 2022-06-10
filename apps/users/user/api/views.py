from rest_framework import generics, status
from rest_framework.response import Response

from .serializers.user_serializers import CreateUserSerializer

class RegisterUserView(generics.CreateAPIView):
    serializer_class=CreateUserSerializer

    def post(self, request, *args, **kwargs):
        user_serialize = self.get_serializer(data=request.data, context={'request': request})
        if user_serialize.is_valid():
            user_serialize.save()
            return Response(user_serialize.data,status=status.HTTP_200_OK)
        return Response(user_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
