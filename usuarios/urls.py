from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/porteiro/', views.cadastrar_porteiro, name="cadastrar_porteiro"),
    path('cadastrar/administrador/', views.cadastrar_adm, name="cadastrar_adm"),
    path('cadastrar/sindico/', views.cadastrar_sindico, name="cadastrar_sindico"),
    path('listar/porteiro/', views.listar_porteiro, name="listar_porteiro"),
    path('listar/adm/', views.listar_adm, name="listar_adm"),
    path('acessar/colaborador/', views.acessar_colaborador, name="acessar_colaborador"),
    path('login/', views.login, name="login"),
    path("recuperar_senha/", views.recuperar_senha, name="recuperar_senha"),
    path('sair/', views.logout, name="sair"),
    path('excluir_usuario/<str:id>/', views.excluir_usuario, name="excluir_usuario"),
]

#todo: fazer a edicão de cadastro de usuário

# action="{% url 'cadastrar_porteiro' %}"