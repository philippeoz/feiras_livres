from rest_framework import status

from django.urls import reverse

from django.test import TestCase

from core.models import FeiraLivre

from tests.test_base import client


class DeleteSingleFeiraLivreTest(TestCase):
    """ Módulo de testes para deletar feiras existentes """

    def setUp(self):
        self.feira_um = FeiraLivre.objects.create(
            nome_feira='feira teste 1')
        self.feira_dois = FeiraLivre.objects.create(
            nome_feira='feira teste 2')

    def test_valid_delete_feira(self):
        response = client.delete(reverse(
            'feira_delete_update_retrieve', kwargs={'pk': self.feira_dois.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_feira(self):
        response = client.delete(
            reverse('feira_delete_update_retrieve', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
