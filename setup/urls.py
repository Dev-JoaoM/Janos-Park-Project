from django.contrib import admin
from django.urls import path

# from cadastros.views import home, CadastroListView, CadastroCreateView, CadastroUptadeView, CadastroDeleteView, CadastroCompleteView
from cadastros.views import *


        # SEPARAÇÃO DAS URLS EM LISTAS DIFERENTES

url_funcionarios = [
    path("funcionarios-lista/", FuncionarioListView.as_view(),name="funcionarios_lista"),
    path("funcionarios-cadastro/", FuncionarioCreateView.as_view(), name="funcionarios_cadastro",),
    path("funcionarios-edicao/<int:pk>", FuncionarioUptadeView.as_view(), name="funcionarios_edicao",),
    path("funcionarios-exclucao/<int:pk>", FuncionarioDeleteView.as_view(), name="funcionarios_exclusao",),
    path("funcionarios-demissao/<int:pk>", FuncionarioDemissoaView.as_view(), name="funcionarios_demissao",),
    path("funcionarios-detalhes/<int:pk>", FuncionarioDetalhesView.as_view(), name="funcionarios_detalhes",),
    # TODO: criar uma tela para detalhar as informações
]

url_apartamentos = [
    path("apartamentos-lista/", ApartamentoListView.as_view(),name="apartamentos_lista"),
    path("apartamentos-cadastro/", ApartamentoCreateView.as_view(), name="apartamentos_cadastro",),
    path("apartamentos-edicao/<int:pk>", ApartamentoUptadeView.as_view(), name="apartamentos_edicao",),
    path("apartamentos-exclucao/<int:pk>", ApartamentoDeleteView.as_view(), name="apartamentos_exclusao",)
]

url_moradores = [
    path("moradores-lista/", MoradorListView.as_view(),name="moradores_lista"),
    path("moradores-cadastro/", MoradorCreateView.as_view(), name="moradores_cadastro",),
    path("moradores-edicao/<int:pk>", MoradorUptadeView.as_view(), name="moradores_edicao",),
    path("moradores-exclucao/<int:pk>", MoradorDeleteView.as_view(), name="moradores_exclusao",)
]

url_visitantes = [
    path("visitantes-lista/", VisitanteListView.as_view(), name="visitantes_lista"),
    path("visitantes-cadastro/", VisitanteCreateView.as_view(), name="visitantes_cadastro",),
    path("visitantes-edicao/<int:pk>", VisitanteUptadeView.as_view(), name="visitantes_edicao",),
    path("visitantes-exclucao/<int:pk>", VisitanteDeleteView.as_view(), name="visitantes_exclusao",)
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),

    # configura o final do caminho por uma variavel que contém o numero do id ou da pk
    # path(caminho_do_link,nome da view --> template.html)
] + url_funcionarios + url_apartamentos + url_moradores + url_visitantes