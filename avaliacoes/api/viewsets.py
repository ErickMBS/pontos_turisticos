from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from .serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacao


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
