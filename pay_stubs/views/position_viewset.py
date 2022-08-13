from rest_framework import viewsets

from pay_stubs.models.position import Position
from pay_stubs.serializers.position_serializer import PositionSerializer


class PositionViewSet(viewsets.ModelViewSet):

    queryset = Position.objects.all()
    serializer_class = PositionSerializer