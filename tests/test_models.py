from django.test import TestCase

from core.models import FeiraLivre


class FeiraLivreTest(TestCase):
    """ Módulo de testes para o model FeiraLivre """

    def create_feira_livre(self):
        return FeiraLivre.objects.create(
            nome_feira="DEINFO_AB_FEIRASLIVRES_2014",
            descricao="Controle de feiras e mercados",
            nivel_agregacao="Logradouro",
            responsavel="SMDU/Deinfo",
            data_referencia="2014-12-21",
            sigilo="0"
        )

    def test_feira_livre_creation(self):
        feira = self.create_feira_livre()

        self.assertTrue(isinstance(feira, FeiraLivre))

    def test_string_representation(self):
        feira = self.create_feira_livre()

        self.assertEqual(str(feira), feira.nome_feira)

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(FeiraLivre._meta.verbose_name_plural), "feiras livres")
