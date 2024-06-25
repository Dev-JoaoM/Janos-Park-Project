from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # TODO: verificar



# from cadastros.views import home, CadastroListView, CadastroCreateView, CadastroUptadeView, CadastroDeleteView, CadastroCompleteView
from cadastros.views import *

urlpatterns = [
    path("admin/", admin.site.urls, name="login_admin"),
    path("", home, name="home"),
    path("home/portaria/", home_portaria, name="index"),
    path('home/admin/', home_admin, name='home_admin'),
    path('home/sindico/', home_sindico, name='home_sindico'),
    path('controle/veiculos/', veiculos_admin, name='veiculos_admin'),
    path('controle_visitas/', controle_visitas, name='controle_visitas'),
    path('controle_visitas_list/', filtro_visitas_controle, name='controle_visitas_list'),
    #path("login/", login, name="login"),
    #path("recuperar_senha/", recuperar_senha, name="recuperar_senha"),
    path('auth/', include('usuarios.urls'))

    # configura o final do caminho por uma variavel que contém o numero do id ou da pk
    # path(caminho_do_link,nome do arq da view --> template.html, name="nome para referenciar essa rota no codigp)
]



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

url_carros_visitantes = [
    path("carros_visitantes-lista/", CarrosVisitanteListView.as_view(), name="carros_visitante_lista"),
    path("carros_visitantes-cadastro/", CarrosVisitanteCreateView.as_view(), name="carros_visitante_cadastro",),
    path("carros_visitantes-edicao/<int:pk>", CarrosVisitanteUptadeView.as_view(), name="carros_visitante_edicao",),
    path("carros_visitantes-exclucao/<int:pk>", CarrosVisitanteDeleteView.as_view(), name="carros_visitante_exclusao",)
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

url_cruds = url_funcionarios + url_apartamentos + url_moradores + url_visitantes + url_carros + url_motos + url_carros_visitantes + url_reg_visitante + url_reg_morador


urlpatterns += url_cruds

