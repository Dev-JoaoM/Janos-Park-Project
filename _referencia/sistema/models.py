from djmoney.models.fields import MoneyField
from django.db import models


class Veiculo(models.Model):
    marca = models.CharField('marca', max_length=100, null=False)
    modelo = models.CharField('modelo', max_length=100, null=False)
    cor = models.CharField('cor', max_length=50, null=False)
    placa = models.CharField('placa', max_length=8, null=False)
    ativo = models.BooleanField('ativo', default=True)
    data_entrada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.placa


class DataEntrada(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.veiculo.data_entrada)


class Valor(models.Model):
    periodoManha = MoneyField(max_digits=14, decimal_places=2,
                              default_currency='BRL', default='2')
    periodoTarde = MoneyField(max_digits=14, decimal_places=2,
                              default_currency='BRL', default='3')
    periodoFDS = MoneyField(max_digits=14, decimal_places=2,
                            default_currency='BRL', default='2.5')

    def __str__(self):
        return "Tabela de Valores"
