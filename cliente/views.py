from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer
from django.shortcuts import render

def cliente_view(request):
    return render(request, 'cliente/cliente.html')

class ClienteView(viewsets.ModelViewSet):

    queryset=Cliente.objects.all()
    serializer_class = ClienteSerializer
