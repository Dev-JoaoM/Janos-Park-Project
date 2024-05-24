# from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy  # usado para acessar as rotas 'path' pelos nomes
from .models import Funcionario, Morador, Apartamento, Visitante  # importação das classes do arquivo models


# Essa é uma FBV: Function Base the View
def home(request):  # recebe uma solicitação
    # cadastros = Cadastro.objects.all()  # Busca as informações no banco
    # nome = ["cleitin", "maria", "joana", "silva"]
    # return render(request, "cadastros/home.html", {"funcionarios": funcionarios, "nome": nome})
    return render(request, "cadastros/home.html") #, {"cadastros": cadastros})
    # renderiza uma template.html com as informações passadas, quando se tem  uma request


# Essas são CBV: Class Base the View
# São mais recomendadas para se utilizar por poder reutilizar a classe pela herança (POO)

            ##### VIEWS DE MORADOR
class FuncionarioListView(ListView):
    model = Funcionario  # Procura um template que tem o mesmo nome da model 'funcionario' acrescido de '_list'


class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ["nome", "dt_nasto", "doc_rg", "doc_cpf", "telefone_apto", "email", "funcao", "dt_admissao", "login", "senha"]
    # campos que o usuário vai poder inserir
    success_url = reverse_lazy("funcionarios_lista")
    # redireciona em caso de sucesso da solicitação


class FuncionarioUptadeView(UpdateView):
    model = Funcionario
    fields = ["nome", "dt_nasto", "doc_rg", "doc_cpf", "telefone_apto", "email", "funcao", "dt_admissao", "login", "senha"]
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
    model = Visitante  # Procura um template que tem o mesmo nome da model 'Morador' acrescido de '_list'


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
    model = Morador
    success_url = reverse_lazy("visitantes_lista")