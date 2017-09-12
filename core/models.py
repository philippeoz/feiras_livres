from django.db import models

from datetime import datetime

from core.utils import parse_date


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

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not isinstance(self.data_referencia, datetime):
            self.data_referencia = parse_date(self.data_referencia)
        super(FeiraLivre, self).save()

    class Meta:
        verbose_name = 'feira livre'
        verbose_name_plural = 'feiras livres'
