from django.views.generic import CreateView, ListView
from django.shortcuts import render, get_object_or_404
from .models import Veiculo, Valor
from .forms import InsereVeiculoForm
from django.urls import reverse_lazy

# Index - Pagina Principa


def index(request):
    return render(request, 'index.html')


class EntradaCreateView(CreateView):
    model = Veiculo
    form_class = InsereVeiculoForm
    template_name = 'entrada.html'
    success_url = reverse_lazy('sistema:veiculos')


class VeiculosListView(ListView):
    template_name = 'veiculos.html'
    model = Veiculo
    context_object_name = 'veiculos'

#ERRO NA SAIDA DE VEICULO COM A MESMA PLACA
def saida(request, placa):
    veiculo = get_object_or_404(Veiculo, placa=placa)
    veiculo.delete()
    return render(request, 'index.html')


def pagar(request, placa):
    veiculo = Veiculo.objects.filter(placa=placa)
    context = {'placa': placa, 'veiculos': veiculo}
    return render(request, 'pagamento.html', context=context)


def veiculo(request, placa):
    veiculos = Veiculo.objects.filter(placa=placa)
    context = {'placa': placa, 'veiculos': veiculos}
    return render(request, 'veiculo.html', context=context)


def valores(request):
    return render(request, 'valores.html')


def tabela(request):
    Valor.objects.create()
    return render(request, 'tabela.html')
