

from django.db import models


class Employee(models.Model):
    """Essa classe representa os fúcionários e seus atributos."""

    CD = 10
    EBI = 20
    DMS = 30
    DMP = 31
    DJ = 32
    GP = 50
    POSITION_CHOICES = [
        (CD, 'Cientista de Dados'),
        (EBI, 'Especialista em Business Intelligence'),
        (DMS, 'Desenvolvedor Mobile Sênior'),
        (DMP, 'Desenvolvedor Mobile Pleno'),
        (DJ, 'Desenvolvedor Junior'),
        (GP, 'Gerente de Projetos')
    ]
    A = 'Ativo'
    I = 'Inativo'
    STATUS_CHOICES = [
        (A, 'Ativo'),
        (I, 'Inativo')
    ]

    registration = models.CharField(
        "Matrícula", primary_key=True, max_length=6, unique=True, editable=False)
    position_code = models.IntegerField(
        "Cargo", choices=POSITION_CHOICES, null=False)
    name = models.CharField("Nome", max_length=100)
    cpf = models.CharField("CPF", max_length=11, unique=True)
    date_admission = models.DateField("Data de admissão", null=False)
    commission = models.BooleanField("Comissão", null=False)
    active_registration = models.CharField(
        "Status", max_length=7, choices=STATUS_CHOICES, null=False)
