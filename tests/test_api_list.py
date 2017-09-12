from rest_framework import status

from django.urls import reverse

from core.models import FeiraLivre

from rest_api.serializers import FeiraLivreSerializer

from tests.test_base import BaseFeiraLivreTest
from tests.test_base import client


class FeiraLivreListTest(BaseFeiraLivreTest):
    """ Módulo de testes para o GET de listagem """

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('feira_list'))
        # get data from db
        feiras = FeiraLivre.objects.all()
        serializer = FeiraLivreSerializer(feiras, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
