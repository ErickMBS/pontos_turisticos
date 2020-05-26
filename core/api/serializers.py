from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from atracoes.api.serializers import AtracaoSerializer
from core.models import PontoTuristico
from atracoes.models import Atracao


class PontoTuristicoSerializer(ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer(read_only=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id',
            'nome',
            'descricao',
            'aprovado',
            'foto',
            'atracoes',
            'comentarios',
            'endereco',
            'avaliacoes',
            'descricao_completa',
            'descricao_completa2',
        )

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        return ponto


    def get_descricao_completa(self, obj):
        return f'{obj.nome} - {obj.descricao}'
