

from uuid import uuid4
from django.db import models

from pay_stubs.models.employee import Employee


class PayStubs(models.Model):
    """Essa classe representa os holerites e seus atributos."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='Matrícula', verbose_name='Matrícula')
    date = models.DateField("Data de referência", null=False)
    absences = models.IntegerField("Faltas", default=0)
    absentee_discount = models.FloatField("Desconto de faltas", null=True)
    fgts_base = models.FloatField("Base de Cáculo FGTS", null=True)
    fgts = models.FloatField("FGTS", null=True)
    inss_base = models.FloatField("Base de Cáculo INSS", null=True)
    inss_discount = models.FloatField("Desconto INSS", null=True)
    inss_aliquot = models.FloatField("Alíquota INSS", null=True)
    irrf_base = models.FloatField("Base de Cáculo IRRF", null=True)
    irrf_discount = models.FloatField("Desconto IRRF", null=True)
    irrf_aliquot = models.FloatField("Alíquota IRRF", null=True)
    total_discount = models.FloatField("Desconto total", null=True)
    total_salaries = models.FloatField("Vencimentos totais", null=True)
    salary_recievable = models.FloatField("Líquido a receber", null=True)
