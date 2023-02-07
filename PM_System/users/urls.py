from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/', UserAPIDetailView.as_view()),
    path('post/', UserCreateView.as_view()),

]