from django.urls import path
from . import views

urlpatterns = [
    path('pecas/', views.PecasSerializer, name='pecas'),

]