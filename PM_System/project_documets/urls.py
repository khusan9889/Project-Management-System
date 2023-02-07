from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/', ProjectDocumentAPIDetailView.as_view()),
    path('post/', ProjectCreateAPIView.as_view()),
    
]
