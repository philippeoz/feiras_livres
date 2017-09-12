from rest_framework import status

from django.test import TestCase

from django.urls import reverse

from core.models import FeiraLivre

from tests.test_base import client

from rest_api.serializers import FeiraLivreSerializer


class FeiraLivreRetrieveTest(TestCase):
    """ Módulo de teste para o GET de uma só FeiraLivre """

    def setUp(self):
        self.feira_um = FeiraLivre.objects.create(nome_feira='Feira test1')
        self.feira_dois = FeiraLivre.objects.create(nome_feira='Feira test2')
        self.feira_tres = FeiraLivre.objects.create(nome_feira='Feira test3')
        self.feira_quatro = FeiraLivre.objects.create(nome_feira='Feira test4')

    def test_get_valid_single_puppy(self):
        response = client.get(reverse(
            'feira_delete_update_retrieve', kwargs={'pk': self.feira_um.pk}))
        feira = FeiraLivre.objects.get(pk=self.feira_um.pk)
        serializer = FeiraLivreSerializer(feira)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_puppy(self):
        response = client.get(
            reverse('feira_delete_update_retrieve', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
