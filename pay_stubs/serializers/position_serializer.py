from rest_framework import serializers
from pay_stubs.models.position import Position

class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'   

    