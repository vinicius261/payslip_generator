
from rest_framework.test import APITestCase

from pay_stubs.models.employee import Employee
from pay_stubs.support_code.test_empolyee_support import employees, employee4


class EmployeeTestCase(APITestCase):

    """Essa classe executa os testes unitários relacionados aos funcionários."""

    def setUp(self):
        for employee in employees:
            post_employee = self.client.post('/funcionarios', employee, format='json')    

    def test_create(self):
        response = self.client.post('/funcionarios', employee4, format='json')

        self.assertEquals(response.status_code, 201)

    def test_delete(self):
        response = self.client.delete('/funcionarios/000001', format='json')

        self.assertEquals(response.status_code, 204)

    def test_delete_status(self):
        delete = self.client.delete('/funcionarios/000001', format='json')
        response = self.client.get('/funcionarios/000001', format='json')

        self.assertEquals(response.data['active_registration'], 'Inativo')

    def test_list(self):
        delete = self.client.delete('/funcionarios/000001', format='json')

        count = len(Employee.objects.filter(active_registration="Ativo"))

        response = self.client.get('/funcionarios', format='json')

        self.assertEquals(response.data['count'], count)
