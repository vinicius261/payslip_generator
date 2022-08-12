
from rest_framework import viewsets, status
from rest_framework.response import Response

from pay_stubs.models.position import Position
from pay_stubs.models.employee import Employee
from pay_stubs.models.pay_stubs import PayStubs

from pay_stubs.serializers.pay_stubs_serializer import PayStubsSerializer
from pay_stubs.support_code.pay_stubes_code import *


class PayStubsViewSet(viewsets.ModelViewSet):
    queryset = PayStubs.objects.all()
    serializer_class = PayStubsSerializer

    def create(self, request, *args, **kwargs):
        """Essa essa sobrescrição do método calcula e persiste holerites. """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee_ = serializer.validated_data['employee_id']
        employee_registration = employee_.pk
        absences = serializer.validated_data['absences']

        employee = Employee.objects.filter(registration=employee_registration)
        employee_position = employee[0].position_code
        base_salary = Position.objects.filter(
            code=employee_position).values_list('base_salary')
        commission_ = (Position.objects.filter(
            code=employee_position).values_list('commission'))
        commission = base_salary[0][0] * commission_[0][0]
        absences_ = float(absences)

        fgts_base,  fgts = calcula_FGTS(base_salary[0][0], commission)
        inss_base, inss_discount, inss_aliquot = calcula_desconto_INSS(
            base_salary[0][0], commission)
        irrf_base, irrf_discount, irrf_aliquot = calcula_IRRF(
            inss_discount, base_salary[0][0], commission)

        absentee_discount = round((base_salary[0][0]/30)*absences_, 2)

        total_discount = round(
            inss_discount + irrf_discount + absentee_discount, 2)

        total_salaries = base_salary[0][0] + commission

        salary_recievable = total_salaries - total_discount

        serializer.validated_data['absentee_discount'] = absentee_discount
        serializer.validated_data['fgts_base'] = fgts_base
        serializer.validated_data['fgts'] = fgts
        serializer.validated_data['inss_base'] = inss_base
        serializer.validated_data['inss_discount'] = inss_discount
        serializer.validated_data['inss_aliquot'] = inss_aliquot
        serializer.validated_data['irrf_base'] = irrf_base
        serializer.validated_data['irrf_discount'] = irrf_discount
        serializer.validated_data['irrf_aliquot'] = irrf_aliquot
        serializer.validated_data['total_discount'] = total_discount
        serializer.validated_data['total_salaries'] = total_salaries
        serializer.validated_data['salary_recievable'] = salary_recievable

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
