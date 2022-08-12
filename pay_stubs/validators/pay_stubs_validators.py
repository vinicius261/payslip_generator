
from rest_framework import serializers

from pay_stubs.models.employee import Employee

def date_(self, data):
    registration = str(data['employee_id']).split()[2].lstrip('(').rstrip(')')
    date_admission = Employee.objects.filter(registration=registration).values_list('date_admission')
    if date_admission[0][0] > data['date']:
        raise serializers.ValidationError({'Data de referência':'Insira uma data posterioir a de contratação.'})

    return data    

def absences_(self, absences):
    if absences >= 10:
        raise serializers.ValidationError('Por favor, corrija o número de faltas ou procure o time de People.') 

    return absences    