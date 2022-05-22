from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView)
from .serializers import articuloSerializers
from .models import articulo

class ArticulosApiView(ListAPIView):

    serializer_class=articuloSerializers
   
    def get_queryset(self):
        return articulo.objects.all()

class ArticulosAgregarView(CreateAPIView):

    serializer_class=articuloSerializers

class ArticulosDetalladoView(RetrieveAPIView):
    
    serializer_class=articuloSerializers
    queryset=articulo.objects.filter()

class ArticulosEliminarView(DestroyAPIView):

    serializer_class=articuloSerializers

    queryset=articulo.objects.all()

class ArticuloActualizarView(RetrieveUpdateAPIView):

    serializer_class=articuloSerializers
    queryset=articulo.objects.all()


