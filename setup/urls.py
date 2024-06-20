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

url_carros = [
    path("carros-lista/", CarroListView.as_view(), name="carros_lista"),
    path("carros-cadastro/", CarroCreateView.as_view(), name="carros_cadastro",),
    path("carros-edicao/<int:pk>", CarroUptadeView.as_view(), name="carros_edicao",),
    path("carros-exclucao/<int:pk>", CarroDeleteView.as_view(), name="carros_exclusao",)
]

url_motos = [
    path("motos-lista/", MotoListView.as_view(), name="motos_lista"),
    path("motos-cadastro/", MotoCreateView.as_view(), name="motos_cadastro",),
    path("motos-edicao/<int:pk>", MotoUptadeView.as_view(), name="motos_edicao",),
    path("motos-exclucao/<int:pk>", MotoDeleteView.as_view(), name="motos_exclusao",)
]


url_reg_visitante = [
    path("registro_visitantes-lista/", RegistroVisitanteListView.as_view(), name="registro_visitantes_lista"),
    path("registro_visitantes-cadastro/", RegistroVisitanteCreateView.as_view(), name="registro_visitantes_cadastro",),
    path("registro_visitantes-edicao/<int:pk>", RegistroVisitanteUptadeView.as_view(), name="registro_visitantes_edicao",),
    path("registro_visitantes-exclucao/<int:pk>", RegistroVisitanteDeleteView.as_view(), name="registro_visitantes_exclusao",)
]

url_reg_morador = [
    path("registro_moradores-lista/", RegistroMoradorListView.as_view(), name="registro_moradores_lista"),
    path("registro_moradores-cadastro/", RegistroMoradorCreateView.as_view(), name="registro_moradores_cadastro",),
    path("registro_moradores-edicao/<int:pk>", RegistroMoradorUptadeView.as_view(), name="registro_moradores_edicao",),
    path("registro_moradores-exclucao/<int:pk>", RegistroMoradorDeleteView.as_view(), name="registro_moradores_exclusao",)
]


urlpatterns = [
    path("admin/", admin.site.urls, name="login_admin"),
    path("", home, name="home"),
    path("home_portaria/", home_portaria, name="index"),
    path('home_admin/', home_admin, name='home_admin'),
    path('controle_veiculos/', veiculos_admin, name='veiculos_admin'),
    path("login/", login, name="login")
    # configura o final do caminho por uma variavel que contém o numero do id ou da pk
    # path(caminho_do_link,nome do arq da view --> template.html, name="nome para referenciar essa rota no codigp)
] + url_funcionarios + url_apartamentos + url_moradores + url_visitantes + url_carros + url_motos + url_reg_visitante + url_reg_morador
