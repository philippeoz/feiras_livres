from django.db import models


class FeiraLivre(models.Model):
    """
    Model FeiraLivre
    Define os atributos de uma feira livre
    """
    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    nível_agregação = models.CharField(max_length=255, null=True, blank=True)
    responsavel = models.CharField(max_length=255, null=True, blank=True)
    data_referencia = models.DateField(null=True, blank=True)
    sigilo = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome
