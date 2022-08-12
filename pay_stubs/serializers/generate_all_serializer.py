from rest_framework import serializers

from pay_stubs.models.pay_stubs import PayStubs


class GenerateAllSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PayStubs
        fields = ['date']