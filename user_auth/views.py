from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer

class CreateUser(CreateAPIView):
    """
        Creates a new User
    """
    serializer_class=UserSerializer
