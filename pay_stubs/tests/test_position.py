
# from rest_framework.test import APITestCase

# position = {
#             "code": 101,
#             "description": "Especialista em Marketing",
#             "base_salary": 30000.0,
#             "commission": 0.8
#             }

# class PositionTestCase(APITestCase):
# """Essa classe executa os testes unitários relacionados aos funcionários."""

#     def test_create(self):
#         response = self.client.post('/cargos/', position, format='json')

#         self.assertEqual(response.status_code, 405)

#     def test_create_message(self):
#         response = self.client.post('/cargos/', position, format='json')

#         self.assertEqual(response.data, 'Não é possível alterar cargos.')

#     def test_update(self):
#         post = self.client.post('/cargos/', position, format='json')
#         response = self.client.put('/cargos/', position, format='json')

#         self.assertEqual(response.status_code, 405)

#     def test_destroy(self):
#         response = self.client.delete('/cargos/', position, format='json')

#         self.assertEqual(response.status_code, 405)
