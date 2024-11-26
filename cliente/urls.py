from django.urls import path
from . import views

urlpatterns = [
    path('cliente/', views.ClienteSerializer, name='cliente'),
]

