from django.shortcuts import render
from rest_framework import generics
from .models import Speciality
from .serializers import SpecialitySerializer
# Create your views here.


#GET, PUT, DELETE
class SpecialityAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

#POST 
class SpecialityCreateView(generics.CreateAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer