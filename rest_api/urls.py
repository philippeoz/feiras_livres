from django.conf.urls import url

from rest_api.views import FeiraLivreViewSet


feira_delete_update = FeiraLivreViewSet.as_view({
    'put': 'update',
    'delete': 'destroy'
})

feira_list = FeiraLivreViewSet.as_view({
    'post': 'create',
    'get': 'list'
})


urlpatterns = [
    # Update, Delete
    url(r'^(?P<pk>[0-9]+)/$', feira_delete_update, name='feira_delete_update'),


    # List, Create
    url(r'^', feira_list, name='feira_list'),

    # Busca
    url(r'^(?P<pk>[0-9]+)/saque/$',
        FeiraLivreViewSet.as_view({'post': 'saque'})),
]
