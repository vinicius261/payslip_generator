from rest_framework import serializers
from pay_stubs.models.position import Position


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    """Essa classe é responsável pela serialização e validação das requisições
        relacionadas a aos cargos."""
    class Meta:
        model = Position
        fields = '__all__'
