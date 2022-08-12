from rest_framework import serializers
from ..models.employee import Employee
from pay_stubs.models.pay_stubs import PayStubs

class PayStubsSerializer(serializers.HyperlinkedModelSerializer):

    absentee_discount = serializers.FloatField(read_only =True)
    fgts_base = serializers.FloatField(read_only =True)
    fgts = serializers.FloatField(read_only =True)
    inss_base = serializers.FloatField(read_only =True)
    inss_discount = serializers.FloatField(read_only =True)
    inss_aliquot = serializers.FloatField(read_only =True)   
    irrf_base = serializers.FloatField(read_only =True)
    irrf_discount = serializers.FloatField(read_only =True)
    irrf_aliquot = serializers.FloatField(read_only =True)
    total_discount = serializers.FloatField(read_only =True)
    total_salaries = serializers.FloatField(read_only =True)
    salary_recievable = serializers.FloatField(read_only =True)  

    class Meta:
        model = PayStubs
        fields = '__all__'

    def validate(self, data):
        registration = str(data['employee_id']).split()[2].lstrip('(').rstrip(')')
        date_admission = Employee.objects.filter(registration=registration).values_list('date_admission')
        if date_admission[0][0] > data['date']:
            raise serializers.ValidationError({'Data de referência':'Insira uma data posterioir a de contratação.'})

        return data    

    def validate_absences(self, absences):
        if absences >= 10:
            raise serializers.ValidationError('Por favor, corrija o número de faltas ou procure o time de People.') 

        return absences    