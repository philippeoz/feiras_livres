from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from core.models import FeiraLivre

from rest_api.serializers import FeiraLivreSerializer


class MultipleFieldLookupMixin(object):
    """
    Mixin para utlizar um ou mais filtros ao realizar uma busca
    """

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:
                filter[field] = self.kwargs[field]
        return get_object_or_404(queryset, **filter)


class FeiraLivreViewSet(viewsets.ModelViewSet,
                        MultipleFieldLookupMixin):
    """
    retrieve:
    Retorna a FeiraLivra de acordo com o id fornecido

    list:
    Retorna uma lista com todas as FeirasLivres existentes

    create:
    Cria uma FeiraLivre
    """
    serializer_class = FeiraLivreSerializer
    model = FeiraLivre

    def get_queryset(self):
        return self.model.objects.all()

    def retrieve(self, request, pk=None):
        queryset = self.model.objects.all()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = self.model.objects.all()
        obj = get_object_or_404(queryset, pk=pk)
        self.perform_destroy(obj)
        return Response(status=200)

    def update(self, request, pk=None):
        queryset = self.model.objects.all()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.update(obj, serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


feira_livre_resources = FeiraLivreViewSet.as_view({
    'post': 'create',
    'delete': 'destroy'
})
