
from rest_framework import viewsets, status
from rest_framework.response import Response

from pay_stubs.serializers.generate_all_serializer import GenerateAllSerializer

from pay_stubs.models.pay_stubs import PayStubs

import requests

class GenerateAllViewSet(viewsets.ModelViewSet):

    queryset = PayStubs.objects.all()
    serializer_class = GenerateAllSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employees = requests.get("http://127.0.0.1:8000/funcionarios")
        employees = employees.json()

        for object in employees['results']:
            data = {
                "date": serializer.validated_data['date'],
                "absences": 0,
                "employee_id": object['url']
                }
            requests.post("http://127.0.0.1:8000/holerites", data=data)

        response = requests.get("http://127.0.0.1:8000/holerites")

        response = response.json()    
            
        headers = self.get_success_headers(response)
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)