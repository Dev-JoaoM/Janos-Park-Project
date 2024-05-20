# from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy  # usado para acessar as rotas 'path' pelos nomes
from .models import Funcionario  # importação da class 'Cadastro' do arquivo models


# Essa é uma FBV: Function Base the View
def home(request):  # recebe uma solicitação
    # cadastros = Cadastro.objects.all()  # Busca as informações no banco
    return render(request, "cadastros/home.html") #, {"cadastros": cadastros})
    # renderiza uma template.html com as informações passadas
    # TODO: Ver o que está aparecendo no template da home (listagem de cadastro ou funcionario)

"""Essa é uma CBV: Class Base the View
São mais recomendadas para se utilizar por poder reutilizar a classe pela herança (POO)"""


class FuncionarioListView(ListView):
    model = Funcionario  # Procura um template que tem o mesmo nome da model 'funcionario' acrescido de '_list'
    # TODO: mudar o nome do template Cadastro_list


class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ["nome", "dt_nasto", "doc_rg", "doc_cpf", "funcao", "dt_admissao", "login", "senha"]
    # campos que o usuário vai poder inserir
    success_url = reverse_lazy("funcionarios_lista")
    # redireciona em caso de sucesso da solicitação


class FuncionarioUptadeView(UpdateView):
    model = Funcionario
    fields = ["nome", "dt_nasto", "doc_rg", "doc_cpf", "funcao", "dt_admissao", "login", "senha"]
    # campos que o usuário vai poder inserir
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




# Cadastro.objects.get(pk=id) um meio de pegar um item do BD


# data_fim_real = models.DateField(null=True)


""" 
nome = ["cleitin", "maria", "joana", "silva"]
return render(request, "cadastros/home.html", {"funcionarios": funcionarios, "nome": nome})
"""
# return render(request, "cadastros/home.html")
# renderiza a request no arquivo html especificado


"""def listar_funcionarios(request):  # recebe uma solicitação
    nome = ["cleitin", "maria", "joana", "silva"]
    return render(request, "cadastros/home.html", {"nome": nome})
    # envia o 'context' para o arquivo html
"""
