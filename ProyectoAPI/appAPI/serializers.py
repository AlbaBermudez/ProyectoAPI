from dataclasses import fields
from rest_framework import serializers

from .models import articulo

class articuloSerializers(serializers.ModelSerializer):

    class Meta:
        model=articulo
        fields=('__all__')
    
