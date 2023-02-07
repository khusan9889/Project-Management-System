from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User
# Create your views here.


#GET,PUT,DELETE methods
class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#POST method
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

