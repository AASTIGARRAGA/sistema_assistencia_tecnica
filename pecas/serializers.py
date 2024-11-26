from rest_framework import serializers
from .models import Pecas

class PecasSerializer(serializers.ModelSerializer):
     class Meta:
        model=Pecas

        filds=[
            'nome',
            'codigo',
            'preco',
        ]