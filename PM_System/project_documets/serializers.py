from rest_framework import serializers
from .models import Project_document


class ProjectDocumentSerializers(serializers.ModelSerializer):
    class Meta:
        models = Project_document
        fields = '__all__'
