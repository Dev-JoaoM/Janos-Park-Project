# from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy  # usado para acessar as rotas 'path' pelos nomes
from .models import Funcionario, Morador, Apartamento, Visitante, Carro, Moto, RegistroVisitante, RegistroMorador  # importação das classes do arquivo models
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.http.response import HttpResponse


# Essa é uma FBV: Function Base the View
def home(request):  # recebe uma solicitação
    return render(request, "home.html")
    # renderiza um template.html com as informações passadas, quando se tem  uma request


def home_portaria(request): # TODO: mandar o nome do usuario logado
    return render(request, "home_portaria.html") 


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")
        usuario = authenticate(username=nome, password=senha)

        if usuario:
            login_django(request, usuario)
            return render(request, "index.html")
        else:
            return HttpResponse("Dados inválidos! Tente novamente. Se persistir o erro entre em contato com os admin.")



# TODO: fazer funções de criação de obj do tipo user. User.objects.create_user(username, password) -> user.save

            ##### VIEWS DE FUNCIONÁRIOS
class FuncionarioListView(ListView):
    model = Funcionario  # Procura um template que tem o mesmo nome da model 'funcionario' acrescido de '_list'


class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ["nome", "dt_nasto", "doc_rg", "doc_cpf", "telefone_apto", "email", "funcao", "dt_admissao", "login", "senha", "confirm_senha"]
    # campos que o usuário vai poder inserir
    success_url = reverse_lazy("funcionarios_lista")
    # redireciona em caso de sucesso da solicitação


class FuncionarioUptadeView(UpdateView):
    model = Funcionario
    fields = ["nome", "dt_nasto", "doc_rg", "doc_cpf", "telefone_apto", "email", "funcao", "dt_admissao", "login", "senha", "confirm_senha"]
    # campos que o usuário vai poder editar
    success_url = reverse_lazy("funcionarios_lista")


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    success_url = reverse_lazy("funcionarios_lista")


class FuncionarioDemissoaView(View):
    def get(self, request, pk):
        registro = get_object_or_404(Funcionario, pk=pk)
        registro.demitir_funcionario()
        return redirect("funcionarios_lista")
    # TODO: antes de excluir perguntar se quer demitir a pessoa


class FuncionarioDetalhesView(View):
    model = Funcionario
    fields = ["nome", "dt_nasto", "doc_rg", "doc_cpf", "funcao", "dt_admissao", "login", "senha",
              "dt_demissao"]  # campos que o usuário vai poder inserir
    #success_url = reverse_lazy("funcionarios-lista/")
    # TODO: faze o detalhamento do cadastro



# Essas são CBV: Class Base the View
# São mais recomendadas para se utilizar por poder reutilizar a classe pela herança (POO)


##### VIEWS DE APARTAMENTO


class ApartamentoListView(ListView):
    model = Apartamento  # Procura um template que tem o mesmo nome da model 'Apartamento' acrescido de '_list'


class ApartamentoCreateView(CreateView):
    model = Apartamento
    fields = ["bloco", "andar", "numero_apto", "telefone_apto"]
    # campos que o usuário vai poder inserir
    success_url = reverse_lazy("apartamentos_lista")
    # redireciona em caso de sucesso da solicitação


class ApartamentoUptadeView(UpdateView):
    model = Apartamento
    fields = ["bloco", "andar", "numero_apto", "telefone_apto"]
    # campos que o usuário vai poder editar
    success_url = reverse_lazy("apartamentos_lista")


class ApartamentoDeleteView(DeleteView):
    model = Apartamento
    success_url = reverse_lazy("apartamentos_lista")


##### VIEWS DE MORADOR

class MoradorListView(ListView):
    model = Morador  # Procura um template que tem o mesmo nome da model 'Morador' acrescido de '_list'


class MoradorCreateView(CreateView):
    model = Morador
    fields = ["apartamento", "nome", "dt_nasto", "doc_rg", "doc_cpf"]
    # campos que o usuário vai poder inserir
    success_url = reverse_lazy("moradores_lista")
    # redireciona em caso de sucesso da solicitação


class MoradorUptadeView(UpdateView):
    model = Morador
    fields = ["apartamento", "nome", "dt_nasto", "doc_rg", "doc_cpf"]
    # campos que o usuário vai poder editar
    success_url = reverse_lazy("moradores_lista")


class MoradorDeleteView(DeleteView):
    model = Morador
    success_url = reverse_lazy("moradores_lista")
    
##### VIEWS DE VISITANTE

class VisitanteListView(ListView):
    model = Visitante


class VisitanteCreateView(CreateView):
    model = Visitante
    fields = ["morador", "nome", "dt_nasto", "doc_rg", "doc_cpf", "telefone"]
    # campos que o usuário vai poder inserir
    success_url = reverse_lazy("visitantes_lista")
    # redireciona em caso de sucesso da solicitação


class VisitanteUptadeView(UpdateView):
    model = Visitante
    fields = ["morador", "nome", "dt_nasto", "doc_rg", "doc_cpf", "telefone"]
    # campos que o usuário vai poder editar
    success_url = reverse_lazy("visitantes_lista")


class VisitanteDeleteView(DeleteView):
    model = Visitante
    success_url = reverse_lazy("visitantes_lista")


##### VIEWS DE CARRO
class CarroListView(ListView):
    model = Carro


class CarroCreateView(CreateView):
    model = Carro
    fields = ["placa", "modelo", "cor", "morador"]
    # campos que o usuário vai poder inserir
    success_url = reverse_lazy("carros_lista")
    # redireciona em caso de sucesso da solicitação


class CarroUptadeView(UpdateView):
    model = Carro
    fields = ["placa", "modelo", "cor", "morador"]
    # campos que o usuário vai poder editar
    success_url = reverse_lazy("carros_lista")


class CarroDeleteView(DeleteView):
    model = Carro
    success_url = reverse_lazy("carros_lista")


##### VIEWS DE MOTO


class MotoListView(ListView):
    model = Moto


class MotoCreateView(CreateView):
    model = Moto
    fields = ["placa", "modelo", "cor", "morador"]
    success_url = reverse_lazy("motos_lista")


class MotoUptadeView(UpdateView):
    model = Moto
    fields = ["placa", "modelo", "cor", "morador"]
    success_url = reverse_lazy("motos_lista")


class MotoDeleteView(DeleteView):
    model = Moto
    success_url = reverse_lazy("motos_lista")

##### VIEWS DE REGISTRO VISITANTE


class RegistroVisitanteListView(ListView):
    model = RegistroVisitante


class RegistroVisitanteCreateView(CreateView):
    model = RegistroVisitante
    fields = ["visitante", "morador", "autorizacao","data_limite", "funcionario"]
    readonly_fields = ["data_entrada"]
    success_url = reverse_lazy("registro_visitantes_lista")


class RegistroVisitanteUptadeView(UpdateView):
    model = RegistroVisitante
    fields = ["visitante", "morador", "funcionario", "data_limite", "data_saida"]
    readonly_fields = ["data_entrada"]
    success_url = reverse_lazy("registro_visitantes_lista")


class RegistroVisitanteDeleteView(DeleteView):
    model = RegistroVisitante
    success_url = reverse_lazy("registro_visitantes_lista")



##### VIEWS DE REGISTRO MORADORES


class RegistroMoradorListView(ListView):
    model = RegistroMorador


class RegistroMoradorCreateView(CreateView):
    model = RegistroMorador
    fields = ["morador", "funcionario"]
    readonly_fields = ["data_entrada"]
    success_url = reverse_lazy("registro_moradores_lista")


class RegistroMoradorUptadeView(UpdateView):
    model = RegistroMorador
    fields = ["morador", "funcionario"]
    readonly_fields = ["data_entrada"]
    success_url = reverse_lazy("registro_moradores_lista")


class RegistroMoradorDeleteView(DeleteView):
    model = RegistroMorador
    success_url = reverse_lazy("registro_moradores_lista")

def home_admin(request):
    return render(request, 'home_admin.html')

def veiculos_admin(request):
    return render(request, 'veiculosadm.html')
