from rest_framework import generics

from users.serializers import UserCreateSerializer, UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UserRitrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
