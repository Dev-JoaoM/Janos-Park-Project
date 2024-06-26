# from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy  # usado para acessar as rotas 'path' pelos nomes
from .models import Funcionario, Morador, Apartamento, Visitante, Carro, Moto, CarroVisitante, RegistroVisitante, RegistroMorador  # importação das classes do arquivo models
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.http.response import HttpResponse
from rolepermissions.decorators import has_permission_decorator
from datetime import date

def filtro_visitas_controle(request):
    data_hoje = date.today()
    registros = RegistroVisitante.objects.filter(data_limite__lt=data_hoje)
    return render(request, "controle_visitas_list.html", {"registros": registros})


# Essa é uma FBV: Function Base the View
def home(request):  # recebe uma solicitação
    return render(request, "home.html")
    # renderiza um template.html com as informações passadas, quando se tem  uma request
    #<p>Subtítulo: usando render, request e o caminho do arquivo html</p>

@has_permission_decorator('visualizar_registro_visitante') #todo: se não for o porteiro, desabilitar o titulo e os botões de cadastrar
def home_portaria(request):
    #usuario = request.username
    return render(request, "home_portaria.html")#, {'usuario': usuario.username})


def controle_visitas_4_list(request):
    #usuario = request.username
    return render(request, "controle_visitas_4_list.html")#, {'usuario': usuario.username})
def controle_visitas_list(request):
    #usuario = request.username
    return render(request, "controle_visitas_list.html")#, {'usuario': usuario.username})

@has_permission_decorator('cadastrar_apartamento')

def home_admin(request):
    return render(request, 'home_admin.html')

def estacionamento(request):
    total_vagas = 75
    vagas_ocupadas = RegistroVisitante.objects.filter(data_saida__isnull=True).count()
    vagas_livres = total_vagas - vagas_ocupadas
    # visitante_carro = CarroVisitante.objects.all()
    vagas_list = RegistroVisitante.objects.filter(data_saida__isnull=True)

    context = {
        'total_vagas': total_vagas,
        'vagas_ocupadas': vagas_ocupadas,
        'vagas_livres': vagas_livres,
        # 'visitante_carro': visitante_carro,
        'vagas_list': vagas_list,
    }
    return render(request, 'estacionamento.html', context)

@has_permission_decorator('cadastrar_adm')
def home_sindico(request):
    return render(request, 'home_sindico.html')

def controle_visitas(request):
    return render(request, 'controle_visitas.html')


#@has_permission_decorator('visualizar_carro_morador')
def veiculos_admin(request):
    return render(request, 'veiculosadm.html')

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


# Essas são CBV: Class Base the View
# São mais recomendadas para se utilizar por poder reutilizar a classe pela herança (POO)


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
#@has_permission_decorator('visualizar_morador')
class MoradorListView(ListView):
    model = Morador# Procura um template que tem o mesmo nome da model 'Morador' acrescido de '_list'


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
    
    
                    ##### VIEWS DE VISITANTES
#@has_permission_decorator('visualizar_visitante')
class VisitanteListView(ListView):
    model = Visitante


class VisitanteCreateView(CreateView):
    model = Visitante
    fields = ["nome", "dt_nasto", "doc_rg", "doc_cpf", "telefone"]
    # campos que o usuário vai poder inserir
    success_url = reverse_lazy("visitantes_lista")
    # redireciona em caso de sucesso da solicitação


class VisitanteUptadeView(UpdateView):
    model = Visitante
    fields = ["nome", "dt_nasto", "doc_rg", "doc_cpf", "telefone", "status"]
    # campos que o usuário vai poder editar
    success_url = reverse_lazy("visitantes_lista")


class VisitanteDeleteView(DeleteView):
    model = Visitante
    success_url = reverse_lazy("visitantes_lista")


    ##### VIEWS DE CARRO MORADORES
class CarroListView(ListView):
    model = Carro


class CarroCreateView(CreateView):
    model = Carro
    fields = ["morador", "placa", "modelo", "cor"]
    # campos que o usuário vai poder inserir
    success_url = reverse_lazy("carros_lista")
    # redireciona em caso de sucesso da solicitação


class CarroUptadeView(UpdateView):
    model = Carro
    fields = ["morador", "placa", "modelo", "cor"]
    # campos que o usuário vai poder editar
    success_url = reverse_lazy("carros_lista")


class CarroDeleteView(DeleteView):
    model = Carro
    success_url = reverse_lazy("carros_lista")


                    ##### VIEWS DE MOTO MORADORES


class MotoListView(ListView):
    model = Moto


class MotoCreateView(CreateView):
    model = Moto
    fields = ["morador", "placa", "modelo", "cor"]
    success_url = reverse_lazy("motos_lista")


class MotoUptadeView(UpdateView):
    model = Moto
    fields = ["morador","placa", "modelo", "cor"]
    success_url = reverse_lazy("motos_lista")


class MotoDeleteView(DeleteView):
    model = Moto
    success_url = reverse_lazy("motos_lista")

                ##### VIEWS DE CARRO VISITANTES
class CarrosVisitanteListView(ListView):
    model = CarroVisitante

class CarrosVisitanteCreateView(CreateView):
    model = CarroVisitante
    fields = ["visitante", "placa", "modelo", "cor"]
    # campos que o usuário vai poder inserir
    success_url = reverse_lazy("carros_visitante_lista")
    # redireciona em caso de sucesso da solicitação

class CarrosVisitanteUptadeView(UpdateView):
    model = CarroVisitante
    fields = ["visitante", "placa", "modelo", "cor"]
    # campos que o usuário vai poder editar
    success_url = reverse_lazy("carros_visitante_lista")

class CarrosVisitanteDeleteView(DeleteView):
    model = CarroVisitante
    success_url = reverse_lazy("carros_visitante_lista")

        ##### VIEWS DE REGISTRO VISITANTE


class RegistroVisitanteListView(ListView):
    model = RegistroVisitante


class RegistroVisitanteCreateView(CreateView):
    model = RegistroVisitante
    fields = ["visitante", "morador", "autorizacao", "data_limite"]
    readonly_fields = ["data_entrada"]
    success_url = reverse_lazy("registro_visitantes_lista")


class RegistroVisitanteUptadeView(UpdateView):
    model = RegistroVisitante
    fields = ["visitante", "morador", "data_limite", "data_saida"]
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
    fields = ["morador", "funcionario", "data_saida"]
    readonly_fields = ["data_entrada"]
    success_url = reverse_lazy("registro_moradores_lista")


class RegistroMoradorDeleteView(DeleteView):
    model = RegistroMorador
    success_url = reverse_lazy("registro_moradores_lista")
