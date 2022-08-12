from rest_framework import serializers

from pay_stubs.validators.pay_stubs_validators import absences_, date_
from ..models.employee import Employee
from pay_stubs.models.pay_stubs import PayStubs


class PayStubsSerializer(serializers.HyperlinkedModelSerializer):
    """Essa classe é responsável pela serialização e validação das requisições
        relacionadas a aos holerites."""

    absentee_discount = serializers.FloatField(read_only=True)
    fgts_base = serializers.FloatField(read_only=True)
    fgts = serializers.FloatField(read_only=True)
    inss_base = serializers.FloatField(read_only=True)
    inss_discount = serializers.FloatField(read_only=True)
    inss_aliquot = serializers.FloatField(read_only=True)
    irrf_base = serializers.FloatField(read_only=True)
    irrf_discount = serializers.FloatField(read_only=True)
    irrf_aliquot = serializers.FloatField(read_only=True)
    total_discount = serializers.FloatField(read_only=True)
    total_salaries = serializers.FloatField(read_only=True)
    salary_recievable = serializers.FloatField(read_only=True)

    class Meta:
        model = PayStubs
        fields = '__all__'

    def validate(self, data):
        content = date_(self, data)
        return content

    def validate_absences(self, absences):
        content = absences_(self, absences)
        return content
