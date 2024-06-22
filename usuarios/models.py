from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

"""class Users(AbstractUser):
    choices_cargo = (('V', 'Vendedor'),
                     ('G', 'Gerente'))
    cargo = models.CharField(max_length=1, choices=choices_cargo)"""


class Colaborador(AbstractUser):
# username, email, senha (campos padrão da class pai User)
    login = models.CharField(verbose_name="Login", max_length=10, null=True) #username
    #email = models.CharField(verbose_name="Email", max_length=100, null=False, blank=False)
    #senha = models.CharField(verbose_name="Senha", max_length=20, null=False, blank=False)
    #confirm_senha = models.CharField(verbose_name="Confirme a senha", max_length=20, null=False, blank=False, default="senha_confirm")

    nome = models.CharField(verbose_name="Nome", max_length=50, null=True)
    dt_nasto = models.DateField(verbose_name="Data de Nascimento", null=True)
    doc_rg = models.CharField(verbose_name="RG", max_length=9, null=True)
    doc_cpf = models.CharField(verbose_name="CPF", max_length=11, null=True)
    telefone = models.CharField(verbose_name="Telefone", max_length=12, null=True)
    dt_admissao = models.DateField(verbose_name="Data de Admissão", null=True)
    dt_demissao = models.DateField(verbose_name="Data de Demissão", null=True)
    motivo_demissao = models.CharField(verbose_name="Motivo da Demissao", max_length=200, null=True)
    
    choices_status= (
        ('A', 'Ativo(a)'),
        ('I', 'Inativo(a)'))
    
    choices_cargo = (
        ('ADM', 'Administrador(a)'),
		('PTR', 'Porteiro(a)'),
		('SDC', 'Síndico(a)'))

    status = models.CharField(max_length=1, choices=choices_status, null=False, blank=False, default="A")
    cargo = models.CharField(max_length=3, choices=choices_cargo, null=True)

    # TODO: validação de senha
    # TODO: geração de senha

    class Meta:
        verbose_name_plural = "Colaboradores"
        ordering = ["nome"]

    """def demitir_colaborador(self):
        if not self.dt_demissao:
            self.dt_demissao = date.today()
            self.save()"""

    def __str__(self):  # -> str:
        return f"{self.nome}"
