from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_porteiro/', views.cadastrar_porteiro, name="cadastrar_porteiro"),
    path('login2/', views.login, name="login2"),
    path('sair/', views.logout, name="sair"),
    path('excluir_usuario/<str:id>/', views.excluir_usuario, name="excluir_usuario")

]
