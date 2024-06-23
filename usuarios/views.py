"""from curses.ascii import HT
import imp"""
from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators  import has_permission_decorator
#from .models import Users
from .models import Colaborador
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages

@has_permission_decorator('cadastrar_porteiro')
def cadastrar_porteiro(request):
    if request.method == "GET":
        porteiros = Colaborador.objects.filter(cargo="PTR")
        return render(request, 'cadastrar_vendedor.html', {'porteiros': porteiros})
    if request.method == "POST":
        nome = request.POST.get('nome')
        #sobrenome = request.POST.get('sobrenome')
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        rg = request.POST.get('doc_rg')
        cpf = request.POST.get('doc_cpf')
        telefone = request.POST.get('telefone')
        dt_admissao =request.POST.get('dt_admissao')
        cargo =request.POST.get('cargo')

        #TODO: Fazer validações dos dados
        
        user = Colaborador.objects.filter(email=email)

        if user.exists():
            # TODO: Utilizar messages do Django
            return HttpResponse('Email já existe')

        user = Colaborador.objects.create_user(username=usuario, # nome para logar 
                                            email=email,
                                            password=senha,
                                            first_name=nome,
                                            #last_name=sobrenome,
                                            doc_rg = rg,
                                            doc_cpf = cpf,
                                            telefone = telefone,
                                            dt_admissao = dt_admissao,
                                            cargo="PTR")

        # TODO: Redirecionar com uma mensagem
        return HttpResponse('Conta criada')

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('plataforma'))
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            #TODO: Redirecionar com mensagem de erro
            return HttpResponse('Usuário inválido')

        auth.login(request, user)
        return HttpResponse('Usuario logado com sucesso')

def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

@has_permission_decorator('cadastrar_porteiro')
def excluir_usuario(request, id):
    porteiro = get_object_or_404(Colaborador, id=id)
    porteiro.delete()
    messages.add_message(request, messages.SUCCESS, 'porteiro excluido com sucesso')
    return redirect(reverse('cadastrar_porteiro'))

