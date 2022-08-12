from uuid import uuid4
from django.db import models


class Position(models.Model):
    """Essa classe representa os cargos e seus atributos."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    code = models.IntegerField("Código", null=True, editable=True)
    description = models.CharField("Descrição", max_length=100, null=False)
    base_salary = models.FloatField("Salário", null=False)
    commission = models.FloatField("Comissão", null=False)
