from django.test import TestCase, Client
from core.models import FeiraLivre


client = Client()


class BaseFeiraLivreTest(TestCase):
    """ Módulo Base de testes para o Model FairaLivre """

    def setUp(self):
        FeiraLivre.objects.create(nome_feira='Feira teste 1')
        FeiraLivre.objects.create(nome_feira='Feira teste 2')
        FeiraLivre.objects.create(nome_feira='Feira teste 3')
        FeiraLivre.objects.create(nome_feira='Feira teste 4')
