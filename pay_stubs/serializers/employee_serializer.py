
from rest_framework import serializers
from pay_stubs.models.employee import Employee
from ..validators.employee_validator import cpf_, name_


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """Essa classe é responsável pela serialização e validação das requisições
    relacionadas aos funcionários."""

    class Meta:
        model = Employee
        fields = '__all__'   

    def validate_name(self, name):
        content = name_(self, name)
        return content

    def validate_cpf(self, cpf):
        content = cpf_(self, cpf)
        return content

    # def validate_registration(self, registrartion):
    #     verification = Employee.objects.filter(code=registrartion).exists()

    #     if verification == False:
    #         raise serializers.ValidationError(
    #         'Esse cadastro não existe. Verifique o número de matrícula.')

    #     return registrartion    

    # def validate_position_code(self, position_code):
    #     positions = Position.objects.filter(code=position_code)
     
    #     if positions == 0:
    #         raise serializers.ValidationError(
    #         'Esse código de cargo não existe.')

    #     return position_code

    

 
            