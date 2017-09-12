import json
from rest_framework import status
from django.test import TestCase
from django.urls import reverse

from tests.test_base import client


class FeiraLivreCreateTest(TestCase):
    """ Módulo de testes para inserção de novas feiras """

    def setUp(self):
        self.valid_payload = {
            "nome_feira": "Feira Teste",
            "descricao": "Esta é apenas uma feira de testes",
            "nivel_agregacao": "3",
            "responsavel": "Tester",
            "data_referencia": "2014-12-31",
            "sigilo": "3",
            "longitude": "43124",
            "latitude": "1234",
            "setcens": "1",
            "areap": "2",
            "coddist": "3",
            "distrito": "Teste",
            "codsubpref": "555",
            "subpref": "Tester",
            "regiao5": "666",
            "regiao8": "777",
            "registro": "Teste",
            "logradouro": "Mais Testes",
            "numero": "111",
            "bairro": "Bairro",
            "referencia": "Rua 75"
        }

        self.invalid_payload = self.valid_payload.copy()
        self.invalid_payload['nome_feira'] = ''

    def test_create_valid_feira(self):
        response = client.post(
            reverse('feira_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_feira(self):
        response = client.post(
            reverse('feira_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
