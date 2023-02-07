from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/', ProjectAPIDetailView.as_view()),
    path('post/', ProjectCreateView.as_view()),
    
]