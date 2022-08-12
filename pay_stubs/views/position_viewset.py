from rest_framework import viewsets, status
from rest_framework.response import Response

from pay_stubs.models.position import Position
from pay_stubs.serializers.position_serializer import PositionSerializer


class PositionViewSet(viewsets.ModelViewSet):
    """Essa classe tem seus métodos sobrescritos para que não seja possível
    a alterção dos dados de cargos."""

    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def create(self, request, *args, **kwargs):
        content = 'Não é possível alterar cargos.'
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        content = 'Não é possível alterar cargos.'
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        content = 'Não é possível deletar cargos.'
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)
