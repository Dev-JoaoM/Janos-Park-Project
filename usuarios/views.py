#from curses.ascii import HT
#import imp
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rolepermissions.decorators  import has_permission_decorator
from .models import Colaborador
from django.urls import reverse
from django.contrib import auth, messages

#@has_permission_decorator('cadastrar_porteiro')
def cadastrar_usuario(request, input_cargo):
    cargo = input_cargo

    if cargo == 'ADM':
        cargo = 'Administrador(a)'
    elif cargo == 'PTR':
        cargo = 'Porteiro(a)'
    elif cargo == 'SDC':
        cargo = 'Síndico(a)'

    if request.method == "GET":
        user = Colaborador.objects.filter(cargo=input_cargo)
        return render(request, 'cadastrar_usuario.html', {'usuarios': user, 'cargos': cargo})

    if request.method == "POST":
        nome = request.POST.get('nome')
        #sobrenome = request.POST.get('sobrenome')
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        dt_nasto = request.POST.get('dt_nasto')
        senha = request.POST.get('senha')
        rg = request.POST.get('doc_rg')
        cpf = request.POST.get('doc_cpf')
        telefone = request.POST.get('telefone')
        #dt_admissao = request.POST.get('dt_admissao')
        #cargo = request.POST.get('cargo')

        #TODO: Fazer validações dos dados
        
        user = Colaborador.objects.filter(username=usuario)
        user_cpf = Colaborador.objects.filter(doc_cpf=cpf)

        if user.exists() or user_cpf.exists():
            # TODO: Utilizar messages do Django
            return HttpResponse('Nome de usuário ou CPF já existe.')

        user = Colaborador.objects.create_user(username=usuario,
                                            nome=nome,
                                            email=email,
                                            dt_nasto = dt_nasto,
                                            password=senha,
                                            first_name=nome,
                                            #last_name=sobrenome,
                                            doc_rg = rg,
                                            doc_cpf = cpf,
                                            telefone = telefone,
                                            #dt_admissao = dt_admissao,
                                            cargo=input_cargo)

        # TODO: Redirecionar com uma mensagem
        return HttpResponse(f'{nome} cadastrado(a) como {cargo} com sucesso!')

@has_permission_decorator('cadastrar_porteiro')
def cadastrar_porteiro(request):
    cargo = "PTR"
    return cadastrar_usuario(request, cargo)

@has_permission_decorator('cadastrar_adm')
def cadastrar_adm(request):
    cargo = "ADM"
    return cadastrar_usuario(request, cargo)


@has_permission_decorator('cadastrar_sindico')
def cadastrar_sindico(request):
    cargo = "SDC"
    return cadastrar_usuario(request, cargo)



def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('login2')) #"cadastrar_porteiro"
        return render(request, 'login2.html')
    elif request.method == "POST":
        login = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            #TODO: Redirecionar com mensagem de erro
            return HttpResponse('Usuário inválido')

        auth.login(request, user)
        return HttpResponse('Usuário logado com sucesso')

def logout(request):
    request.session.flush()
    return redirect(reverse('login2'))


def excluir_usuario(request, id):
    #cargo = in_cargo
    usuario = get_object_or_404(Colaborador, id=id)
    usuario.delete()

    messages.add_message(request, messages.SUCCESS, 'Usuário excluído com sucesso.')
    return redirect(reverse('cadastrar_adm')) # todo: redirecionar para pagina certa

    """if cargo == 'ADM':
        return redirect(reverse('cadastrar_adm'))

    elif cargo == 'PTR':
        return redirect(reverse('cadastrar_porteiro'))

    elif cargo == 'SDC':
        return redirect(reverse('cadastrar_sindico'))

    return redirect(reverse('cadastrar_' + cargo))"""

"""@has_permission_decorator('cadastrar_porteiro')
def excluir_porteiro(request, id):
    cargo = "PTR"
    return excluir_usuario(request, id, cargo)

@has_permission_decorator('cadastrar_adm')
def excluir_adm(request, id):
    cargo = "ADM"
    return excluir_usuario(request, id, cargo)

@has_permission_decorator('cadastrar_sindico')
def excluir_sindico(request, id):
    cargo = "SDC"
    return excluir_usuario(request, id, cargo)
"""