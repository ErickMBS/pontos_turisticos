from rest_framework.viewsets import ModelViewSet
from .serializers import ComentarioSerializer
from rest_framework import filters
from comentarios.models import Comentario

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ('usuario',)
