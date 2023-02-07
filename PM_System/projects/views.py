from django.shortcuts import render
from rest_framework import generics
from .serializers import ProjectSerializer
from .models import Project
# Create your views here.


#GET,PUT,DELETE methods
class ProjectAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

#POST 
class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer