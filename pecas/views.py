from rest_framework import viewsets
from .models import Pecas
from .serializers import PecasSerializer
from django.shortcuts import render

def pecas_view(request):
    return render(request, 'pecas/pecas.html')
class PecasView(viewsets.ModelViewSet):
    
    queryset=Pecas.objects.all()
    serializer_class = PecasSerializer


