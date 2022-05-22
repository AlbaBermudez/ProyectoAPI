from django.urls import path
from .views import (
    ArticulosAgregarView, ArticulosApiView, ArticulosDetalladoView, ArticulosEliminarView,ArticuloActualizarView)

urlpatterns = [
    path('api/', ArticulosApiView.as_view(), name="Api"),
    path('api/agregar/', ArticulosAgregarView.as_view(), name="create"),
    path('api/detallado/<pk>/', ArticulosDetalladoView.as_view(), name="detail"),
    path('api/eliminar/<pk>/', ArticulosEliminarView.as_view(), name="delete"),
    path('api/actualizar/<pk>/', ArticuloActualizarView.as_view(), name="update"),
   
]
