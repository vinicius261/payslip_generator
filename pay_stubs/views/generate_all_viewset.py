
from this import d
from rest_framework import viewsets, status
from rest_framework.response import Response

from pay_stubs.serializers.generate_all_serializer import GenerateAllSerializer

from pay_stubs.models.pay_stubs import PayStubs

import requests

from ..support_code.generate_all_code import this_month


class GenerateAllViewSet(viewsets.ModelViewSet):

    queryset = PayStubs.objects.all()
    serializer_class = GenerateAllSerializer

    def create(self, request, *args, **kwargs):
        """Essa essa sobrescrição do método cria e persiste holerites no banco para
        todos o funcionários ativos de uma só vez."""

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employees = requests.get("http://127.0.0.1:8000/funcionarios")
        employees = employees.json()

        month = str(serializer.validated_data['date']).split('-')[-2]
        year = str(serializer.validated_data['date']).split('-')[-3]

        inital_date, final_date = this_month(year, month)

        already_generated = requests.get(
                f"http://127.0.0.1:8000/holerites?date__gte={inital_date}&date__lte={final_date}")
        already_generated =already_generated.json()

        ids =[]

        for result in already_generated['results']:
            ids.append(result['employee_id'])

        for object in employees['results']:

            if object['url'] not in ids:
                data = {
                    "date": serializer.validated_data['date'],
                    "absences": 0,
                    "employee_id": object['url']
                }
                requests.post("http://127.0.0.1:8000/holerites", data=data)


        response = requests.get(
            f"http://127.0.0.1:8000/holerites?date__gte={inital_date}&date__lte={final_date}")

        response = response.json()

        headers = self.get_success_headers(response)
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)
