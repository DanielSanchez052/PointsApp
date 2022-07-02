from rest_framework import generics

from .serializers.user_serializers import CreateUserSerializer

class RegisterUserView(generics.CreateAPIView):
    serializer_class=CreateUserSerializer

