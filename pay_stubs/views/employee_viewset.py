from rest_framework import viewsets, status
from rest_framework.response import Response

from pay_stubs.models.employee import Employee
from pay_stubs.serializers.employee_serializer import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['registration'] = str(len(Employee.objects.all())+1).zfill(6)
        serializer.validated_data['active_registration'] = 'Ativo'
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def destroy(self, request, *args, **kwargs):
        status_ = Employee.objects.filter(pk=kwargs['pk'])
        status_.update(active_registration="Inativo")
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    def list(self, request, *args, **kwargs):
        queryset = Employee.objects.filter(active_registration="Ativo")

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
    