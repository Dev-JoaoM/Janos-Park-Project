from django.contrib import admin
from django.urls import path

# from cadastros.views import home, CadastroListView, CadastroCreateView, CadastroUptadeView, CadastroDeleteView, CadastroCompleteView
from cadastros.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("funcionarios-lista/",
         FuncionarioListView.as_view(),
         name="funcionarios_lista"),
    path(
        "funcionarios-cadastro/",
        FuncionarioCreateView.as_view(),
        name="funcionarios_cadastro",
    ),
    path(
        "funcionarios-edicao/<int:pk>",
        FuncionarioUptadeView.as_view(),
        name="funcionarios_edicao",
    ),
    path(
        "funcionarios-exclucao/<int:pk>",
        FuncionarioDeleteView.as_view(),
        name="funcionarios_exclusao",
    ),
    path(
        "funcionarios-demissao/<int:pk>",
        FuncionarioDemissoaView.as_view(),
        name="funcionarios_demissao",
    ),

    path(
        "funcionarios-detalhes/<int:pk>",
        FuncionarioDetalhesView.as_view(),
        name="funcionarios_detalhes",
    ),
    # configura o final do caminho por uma variavel que contém o numero do id ou da pk
    # path(caminho_do_link,nome da view --> template.html)
]




# <a href="{% url 'cadastro_funcionarios' %} " class="btn-primary btn-sm">Novo Cadastro</a>

"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
