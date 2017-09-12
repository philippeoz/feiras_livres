from django.db import models


class FeiraLivre(models.Model):
    """
    Model FeiraLivre
    Define os atributos de uma feira livre
    """
    nome_feira = models.CharField(max_length=255)

    descricao = models.TextField(
        verbose_name='Descrição', null=True, blank=True)

    nivel_agregacao = models.CharField(
        verbose_name='Nível de Agregação',
        max_length=255, null=True, blank=True)

    responsavel = models.CharField(
        verbose_name='Responsável', max_length=255, null=True, blank=True)

    data_referencia = models.DateField(
        verbose_name='Data de Referência', null=True, blank=True)

    sigilo = models.IntegerField(null=True, blank=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    setcens = models.CharField(max_length=255, blank=True, null=True)
    areap = models.CharField(max_length=255, blank=True, null=True)
    coddist = models.CharField(max_length=255, blank=True, null=True)
    distrito = models.CharField(max_length=255, blank=True, null=True)
    codsubpref = models.CharField(max_length=255, blank=True, null=True)
    subpref = models.CharField(max_length=255, blank=True, null=True)
    regiao5 = models.CharField(max_length=255, blank=True, null=True)
    regiao8 = models.CharField(max_length=255, blank=True, null=True)
    registro = models.CharField(max_length=255, blank=True, null=True)
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    referencia = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome_feira

    class Meta:
        verbose_name = 'feira livre'
        verbose_name_plural = 'feiras livres'
