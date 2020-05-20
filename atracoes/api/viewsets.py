from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .serializers import AtracaoSerializer
from atracoes.models import Atracao

class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = AtracaoSerializer

    filter_backends = [SearchFilter]
    search_fields = ('nome', 'descricao')
