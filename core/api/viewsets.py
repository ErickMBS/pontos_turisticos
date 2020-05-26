from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import PontoTuristicoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import PontoTuristico
from rest_framework import status


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao',)
    lookup_field = 'id'  # Necessário ser unique... Se houver mais de um objeto dará erro no get...

    def get_queryset(self):
        id_ponto = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()
        # OBS: isso é lazyload... Ou seja, não vai pegar todos do bd e colocar em queryset... é um 'pré-select'.
        if id_ponto:
            queryset = queryset.filter(id=id_ponto)

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        if descricao:
            queryset = queryset.filter(descricao__icontains=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


    # def create(self, request, *args, **kwargs):
    #     try:
    #         if request.data['aprovado']:
    #             ponto = PontoTuristico.objects.create(
    #                 aprovado=True,
    #                 nome=request.data['nome'],
    #                 descricao=request.data['descricao'],
    #             )
    #             return Response({'Ok': f'Opa, ponto turistico criado, id: {ponto.id}'})
    #         else:
    #             return Response({'Nope': 'Tem que ser aprovado...'})
    #     except Exception as e:
    #         return Response({'Erro': f'Não foi aprovado... erro:{e}'})


    def destroy(self, request, *args, **kwargs):
        objeto = self.get_object()
        PontoTuristico.objects.filter(nome=objeto).update(aprovado=False)
        return Response(status=status.HTTP_204_NO_CONTENT, data='Ponto Turístico removido das visualizações.')


    def retrieve(self, request, *args, **kwargs):
        objeto = self.get_object()
        serializer = self.get_serializer(objeto)
        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        # OBS: a pk pode ser encontrada em kwargs['pk']
        parcial = kwargs.pop('partial', False)

        objeto = self.get_object()
        data = request.data
        serializer = PontoTuristicoSerializer(objeto, data=data, partial=parcial)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)  # não está a funcionar...


    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']
        ponto = PontoTuristico.objects.get(id=id)

        ponto.atracoes.set(atracoes)
        ponto.save()

        return Response('OK', status=status.HTTP_200_OK)
