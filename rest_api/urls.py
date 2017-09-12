from django.conf.urls import url

from rest_api.views import FeiraLivreViewSet


feira_delete_update_retrieve = FeiraLivreViewSet.as_view({
    'put': 'update',
    'delete': 'destroy',
    'get': 'retrieve'
})

feira_list = FeiraLivreViewSet.as_view({
    'post': 'create',
    'get': 'list'
})


urlpatterns = [
    # Busca
    url(r'^busca/$', FeiraLivreViewSet.as_view({'post': 'search'})),

    # Update, Delete, Detail
    url(r'^(?P<pk>[0-9]+)/$',
        feira_delete_update_retrieve, name='feira_delete_update'),

    # List, Create
    url(r'^', feira_list, name='feira_list'),
]
