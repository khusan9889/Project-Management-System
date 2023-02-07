from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/', SpecialityAPIDetailView.as_view()),
    path('post/', SpecialityCreateView.as_view()),

]

