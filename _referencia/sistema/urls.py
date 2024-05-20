from sistema.views import EntradaCreateView, VeiculosListView
from django.urls import path, re_path
from . import views

app_name = 'sistema'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^veiculos/$', VeiculosListView.as_view(), name='veiculos'),
    re_path(r'^veiculo/(?P<placa>[a-zA-Z]{3}-[0-9]{4})/$',
            views.veiculo, name='veiculo'),
    re_path(r'^veiculo/(?P<placa>[a-zA-Z]{3}-[0-9]{4})/saida/$',
            views.saida, name='saida'),
    re_path(r'^veiculo/(?P<placa>[a-zA-Z]{3}-[0-9]{4})/pagar/$',
            views.pagar, name='pagar'),
    re_path(r'^valores/$', views.valores, name='valores'),
    re_path(r'^valores/tabela/$', views.tabela, name='tabela'),
    re_path(r'^entrada/$', EntradaCreateView.as_view(), name='entrada'),
]
