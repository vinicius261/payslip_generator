from rest_framework import serializers
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
         