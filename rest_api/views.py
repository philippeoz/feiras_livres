from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from core.models import FeiraLivre

from rest_api.serializers import FeiraLivreSerializer


class MultipleFieldLookupMixin(object):
    """
    Mixin para utlizar um ou mais filtros ao realizar uma busca
    """

    def search(self, request):
        """
        Método para buscar uma feira utilizando um ou mais parâmetros
        """
        queryset = self.get_queryset()
        filtro = {}
        for field in self.lookup_fields:
            if field in request.data.keys():
                filtro[
                    "{}{}".format(field, '__icontains')
                ] = request.data[field]

        queryset = queryset.filter(**filtro)

        if queryset:
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=400)


class FeiraLivreViewSet(viewsets.ModelViewSet,
                        MultipleFieldLookupMixin):
    """
    retrieve:
    Retorna uma FeiraLivre de acordo com o id fornecido

    destroy:
    Deleta a FeiraLivre de acordo com o id fornecido

    update:
    Atualiza uma FeiraLivre de acordo com o id e
    parâmetros fornecidos via json

    list:
    Retorna uma lista com todas as FeirasLivres existentes

    create:
    Cria uma FeiraLivre
    """
    serializer_class = FeiraLivreSerializer
    model = FeiraLivre
    lookup_fields = [
        'distrito',
        'regiao5',
        'nome_feira',
        'bairro'
    ]

    def get_queryset(self):
        return self.model.objects.all()

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        self.perform_destroy(obj)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.update(obj, serializer.validated_data)
            return Response(serializer.data, status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=400)

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
