
from turtle import position
from rest_framework import serializers
from pay_stubs.models.employee import Employee
from pay_stubs.models.position import Position

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'   

    def validate_name(self, name):
        if len(name.split()) < 2:
            raise serializers.ValidationError('Por favor, insira o nome completo.')
        
        return name

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('Por favor, insira o CPF corretamente.')
        
        return cpf

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

    


            