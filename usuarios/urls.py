from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/porteiro/', views.cadastrar_porteiro, name="cadastrar_porteiro"),
    path('cadastrar/administrador/', views.cadastrar_adm, name="cadastrar_adm"),
    path('cadastrar/sindico/', views.cadastrar_sindico, name="cadastrar_sindico"),
    path('login2/', views.login, name="login2"),
    path('sair/', views.logout, name="sair"),
    #path('/',  name="home"),
    path('excluir_usuario/<str:id>/', views.excluir_usuario, name="excluir_usuario")

]
# action="{% url 'cadastrar_porteiro' %}"