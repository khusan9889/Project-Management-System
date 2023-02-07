from django.shortcuts import render
from rest_framework import generics
from .serializers import ProjectDocumentSerializers
from .models import Project_document

# Create your views here.


#GET,PUT,DELETE methods
class ProjectDocumentAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project_document.objects.all()
    serializer_class = ProjectDocumentSerializers


class ProjectCreateAPIView(generics.CreateAPIView):
    queryset = Project_document.objects.all()
    serializer_class = ProjectDocumentSerializers