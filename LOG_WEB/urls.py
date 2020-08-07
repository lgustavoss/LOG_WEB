from django.conf.urls import url
from .views import *

urlpatterns = [
   url(r'^listar_estabelecimento/', listar_estabelecimento, name='estabelecimento_list'),
   url(r'^cadastrar_estabelecimento/', cadastrar_estabelecimento, name='cadastrar_estabelecimento'),
   url(r'^editar_estabelecimento/(?P<pk>[0-9]+)', editar_estabelecimento, name='editar_estabelecimento'),
]