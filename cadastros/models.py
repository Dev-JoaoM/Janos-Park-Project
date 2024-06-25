from django.db import models
from datetime import date, timedelta, datetime
from usuarios.models import Colaborador

class Cadastro(models.Model):
    titulo = models.CharField(
        verbose_name="Nome", max_length=50, null=False, blank=False
    )
    data = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    datafim = models.DateField(
        verbose_name="Data de Nascimento", null=False, blank=False
    )
    data_fim_real = models.DateField(null=True)

    class Meta:
        ordering = ["datafim"]

    def mark_has_complete(self):
        if not self.data_fim_real:
            self.data_fim_real = date.today()
            self.save()

class Funcionario(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=50, null=False, blank=False)
    dt_nasto = models.DateField(verbose_name="Data de Nascimento", null=False, blank=False)
    doc_rg = models.CharField(verbose_name="RG", max_length=9, null=False, blank=False)
    doc_cpf = models.CharField(verbose_name="CPF", max_length=11, null=False, blank=False)
    telefone_apto = models.CharField(verbose_name="Telefone", max_length=12, null=False, blank=False)
    email = models.CharField(verbose_name="Email", max_length=100, null=False, blank=False)
    funcao = models.CharField(verbose_name="Função", max_length=15, null=False, blank=False)
    dt_admissao = models.DateField(verbose_name="Data de Admissão", null=False, blank=False)
    dt_demissao = models.DateField(verbose_name="Data de Demissão", null=True)
    motivo_demissao = models.CharField(verbose_name="Motivo da Demissão", max_length=200, null=False, blank=False)
    login = models.CharField(verbose_name="Login", max_length=10, null=False, blank=False)
    senha = models.CharField(verbose_name="Senha", max_length=20, null=False, blank=False)
    confirm_senha = models.CharField(verbose_name="Confirme a senha", max_length=20, null=False, blank=False)
    # status = models.BooleanField(verbose_name="Status", null=False, blank=False, default=True)

    # TODO: validação de senha

    class Meta:
        verbose_name_plural = "funcionarios"
        ordering = ["nome"]

    def demitir_funcionario(self):
        if not self.dt_demissao:
            self.dt_demissao = date.today()
            self.save()

    def __str__(self):  # -> str:
        return f"{self.nome}"


class Apartamento(models.Model):
    bloco = models.CharField(verbose_name="Bloco", max_length=5, null=False, blank=False)
    andar = models.CharField(verbose_name="Andar", max_length=5, null=False, blank=False)
    numero_apto = models.IntegerField(verbose_name="Numero do Apartamento", null=False, blank=False)
    telefone_apto = models.CharField(verbose_name="Telefone", max_length=8, null=False, blank=False)
    """
        choices_status= (
    ('A', 'Ativo(a)'), 
    ('I', 'Inativo(a)'), 

    )

    status = models.CharField(max_length=1, choices=choices_status, null=False, blank=False, default="A")
    """
    def __str__(self):
        return f"Apartamento n° {self.numero_apto}, {self.andar}º andar, bloco {self.bloco}"

class Morador(models.Model):
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)
    nome = models.CharField(verbose_name="Nome", max_length=50, null=False, blank=False)
    dt_nasto = models.DateField(verbose_name="Data de Nascimento", null=False, blank=False)
    doc_rg = models.CharField(verbose_name="RG", max_length=9, null=False, blank=False)
    doc_cpf = models.CharField(verbose_name="CPF", max_length=11, null=False, blank=False)

    """
        choices_status= (
    ('A', 'Ativo(a)'), 
    ('I', 'Inativo(a)'), 

    )

    status = models.CharField(max_length=1, choices=choices_status, null=False, blank=False, default="A")
    """

    def __str__(self):
            return f"{self.nome}"


class Visitante(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=50, null=False, blank=False)
    dt_nasto = models.DateField(verbose_name="Data de Nascimento", null=False, blank=False)
    doc_rg = models.CharField(verbose_name="RG", max_length=9, null=False, blank=False)
    doc_cpf = models.CharField(verbose_name="CPF", max_length=11, null=False, blank=False)
    telefone = models.CharField(verbose_name="Telefone", max_length=8, null=False, blank=False)

    choices_status= (('A', 'Ativo(a)'),('S', 'Suspenso(a)'),('I', 'Inativo(a)'))
    status = models.CharField(max_length=1, choices=choices_status, null=False, blank=False, default="A")

    def __str__(self):
        return (f"{self.nome}")


class RegistroVisitante(models.Model):
    morador = models.ForeignKey(Morador, on_delete=models.DO_NOTHING)  # rever esse parametro
    visitante = models.ForeignKey(Visitante, on_delete=models.DO_NOTHING)  # rever esse parametro
    data_entrada = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_limite = models.DateTimeField(null=True, blank=True) 
    data_saida = models.DateTimeField(null=True)
    autorizacao = models.BooleanField(verbose_name="Autorização do Morador", null=False, blank=False)
    ##funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)  # rever esse parametro
    # TODO: def de saida com um checkbox
    # TODO: Se não tem autorização do morador não tem data de entrada e nem data limite de saida

    class Meta:
        ordering = ["data_limite"]

    def marcar_saida(self):
        if not self.data_saida:
            self.data_saida = datetime.now()
            self.save()

    """
        choices_status= (
    ('A', 'Ativo(a)'), 
    ('I', 'Inativo(a)'), 

    )

    status = models.CharField(max_length=1, choices=choices_status, null=False, blank=False, default="A")
    """

    # TODO: pegar o funcionário que fez o registro de acordo com o login
    # TODO: inserir a data limite por funcao
    # TODO: quando inserir o visitante retornar o carro dele se estiver de carro
    # TODO: não é obrigatório o visitante entrar de carro


class RegistroMorador(models.Model):
    morador = models.ForeignKey(Morador, on_delete=models.DO_NOTHING)  # rever esse parametro
    data_entrada = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_saida = models.DateTimeField(null=True, blank=True)
    #funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)  # rever esse parametro
    class Meta:
        ordering = ["data_saida"]
        
    def marcar_saida(self):
        if not self.data_saida:
            self.data_saida = datetime.now()
            self.save()

    # TODO: def de saida com um checkbox
    """
        choices_status= (
    ('A', 'Ativo(a)'), 
    ('I', 'Inativo(a)'), 

    )

    status = models.CharField(max_length=1, choices=choices_status, null=False, blank=False, default="A")
    """


    # TODO: pegar o funcionário que fez o registro de acordo com o login
    # TODO: quando morador o retornar o carro dele se estiver de carro
    # TODO: não é obrigatório o morador entrar de carro


class QntVagasVisita(models.Model):
    registro_visitante = models.ForeignKey(RegistroVisitante, on_delete=models.DO_NOTHING)  # rever esse parametro
    qnt_vagas = models.IntegerField(null=False, blank=False)
    vagas_disponiveis = models.IntegerField(null=False, blank=False)

    # Talvez não precise do 'vagas_disponiveis' por ser um campo calculado


class Carro(models.Model): #Carros de Moradores
    modelo = models.CharField(verbose_name="Modelo", max_length=10, null=False, blank=False)
    placa = models.CharField(verbose_name="Placa", max_length=8, null=False, blank=False)
    cor = models.CharField(verbose_name="Cor", max_length=10, null=False, blank=False)
    morador = models.ForeignKey(Morador, on_delete=models.DO_NOTHING)
    """
        choices_status= (
    ('A', 'Ativo(a)'), 
    ('I', 'Inativo(a)'), 

    )

    status = models.CharField(max_length=1, choices=choices_status, null=False, blank=False, default="A")
    """


    def __str__(self):
        return f"Placa {self.placa}, {self.modelo},{self.cor}"


class CarroVisitante(models.Model):
    modelo = models.CharField(verbose_name="Modelo", max_length=10, null=False, blank=False)
    placa = models.CharField(verbose_name="Placa", max_length=8, null=False, blank=False)
    cor = models.CharField(verbose_name="Cor", max_length=10, null=False, blank=False)
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)
    """
        choices_status= (
    ('A', 'Ativo(a)'), 
    ('I', 'Inativo(a)'), 

    )

    status = models.CharField(max_length=1, choices=choices_status, null=False, blank=False, default="A")
    """

    def __str__(self):
        return f"Placa {self.placa}, {self.modelo},{self.cor}"


class Moto(models.Model):
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    modelo = models.CharField(verbose_name="Modelo", max_length=10, null=False, blank=False)
    placa = models.CharField(verbose_name="Placa", max_length=8, null=False, blank=False)
    cor = models.CharField(verbose_name="Cor", max_length=10, null=False, blank=False)
    """
        choices_status= (
    ('A', 'Ativo(a)'), 
    ('I', 'Inativo(a)'), 

    )

    status = models.CharField(max_length=1, choices=choices_status, null=False, blank=False, default="A")
    """


    def __str__(self):
        return f"Placa {self.placa}, {self.modelo},{self.cor}, visitante {self.apartamento}"


# As classes representam as tabelas do BD e os atributos das classes representam as colunas da tabela
# Primeiro cria a migração → python manage.py makemigrations
# Depois aplica a migração e cria o arquivo sqlite → python manage.py migrate
# Como se fosse o commit e push do git, para versionar as migrações
