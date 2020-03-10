from django.conf.urls import url
from .views import *

urlpatterns = [
     url(r'^produto/listar/(?P<categoria>[\w\-]+)/$', listar_produto, name='listar_produto'),
     url(r'^produto/perfil/(?P<pk>[0-9]+)', perfil_produto, name='perfil_produto'),
]