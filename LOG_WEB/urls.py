from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
   url(r'^listar_estabelecimento/', listar_estabelecimento, name='listar_estabelecimento'),
   url(r'^listar_colaborador/', listar_colaborador, name='listar_colaborador'),
   url(r'^cadastrar_estabelecimento/', cadastrar_estabelecimento, name='cadastrar_estabelecimento'),
   url(r'^cadastrar_colaborador/', cadastrar_colaborador, name='cadastrar_colaborador'),
   url(r'^editar_estabelecimento/(?P<pk>\d+)', editar_estabelecimento, name='editar_estabelecimento'),
   url(r'^editar_colaborador/(?P<pk>\d+)', editar_colaborador, name='editar_colaborador'),
]