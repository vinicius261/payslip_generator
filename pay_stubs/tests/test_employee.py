
from rest_framework.test import APITestCase

from pay_stubs.models.employee import Employee
true = True

employee = {
    "position_code": 10,
    "name": "Viera Souza",
    "cpf": "40122598966",
    "date_admission": "2022-08-10",
    "commission": true,
    "active_registration": "Inativo"
}

employee2 = {
    "position_code": 31,
    "name": "Viera Siqueira",
    "cpf": "40122598698",
    "date_admission": "2022-08-10",
    "commission": true,
    "active_registration": "Inativo"
}

employee3 = {
    "position_code": 32,
    "name": "Viera Souza",
    "cpf": "40155898966",
    "date_admission": "2022-12-10",
    "commission": true,
    "active_registration": "Inativo"
}


class EmployeeTestCase(APITestCase):

    """Essa classe executa os testes unitários relacionados aos funcionários."""

    def test_create(self):
        response = self.client.post('/funcionarios', employee, format='json')

        self.assertEquals(response.status_code, 201)

    def test_delete(self):
        post = self.client.post('/funcionarios', employee, format='json')
        response = self.client.delete('/funcionarios/000001', format='json')

        self.assertEquals(response.status_code, 204)

    def test_delete_status(self):
        post = self.client.post('/funcionarios', employee, format='json')
        delete = self.client.delete('/funcionarios/000001', format='json')
        response = self.client.get('/funcionarios/000001', format='json')

        self.assertEquals(response.data['active_registration'], 'Inativo')

    def test_list(self):
        post = self.client.post('/funcionarios', employee, format='json')
        post2 = self.client.post('/funcionarios', employee2, format='json')
        post3 = self.client.post('/funcionarios', employee3, format='json')
        delete = self.client.delete('/funcionarios/000001', format='json')

        count = len(Employee.objects.filter(active_registration="Ativo"))

        response = self.client.get('/funcionarios', format='json')

        self.assertEquals(response.data['count'], count)
