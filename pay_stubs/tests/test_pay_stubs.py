from rest_framework.test import APITestCase
from pay_stubs.support_code.test_empolyee_support import employees
from pay_stubs.support_code.test_pstubs_code import pay_stubs, positions

class PayStubsTestCase(APITestCase):
    """Essa classe executa os testes unitários relacionados aos holerites."""
    def setUp(self):
        for position in positions:
            post_position = self.client.post('/cargos', position, format='json')

        for employee in employees:
            post_employee = self.client.post('/funcionarios', employee, format='json')
        
    def test_create(self):        
        response = self.client.post('/holerites', pay_stubs, format='json')

        self.assertEquals(response.status_code, 201)
