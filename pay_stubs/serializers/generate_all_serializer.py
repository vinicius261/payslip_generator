from rest_framework import serializers

from pay_stubs.models.pay_stubs import PayStubs


class GenerateAllSerializer(serializers.HyperlinkedModelSerializer):
    """Essa classe é responsável pela serialização e validação das requisições
        relacionadas a geração de todos holerites de uma só vez."""

    class Meta:
        model = PayStubs
        fields = ['date']
