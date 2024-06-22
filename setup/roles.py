#import imp
from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_produtos': True,
        'liberar_descontos': True,
        'cadastrar_vendedor': True,
    }

class Vendedor(AbstractUserRole):
    available_permissions = {
        'realizar_venda': True,
    }


class Sindico(AbstractUserRole):
    available_permissions = {
        'cadastrar_adm': True,
        'visualizar_porteiro': True,
        'visualizar_apartamento': True,
        'visualizar_morador': True,
        'visualizar_carro_morador': True,
        'visualizar_moto_morador': True,
        'visualizar_visitante': True,
        'visualizar_carro_visitante': True,
        'visualizar_registro_visitante': True,
        'visualizar_registro_morador': True,
        }



class Adm(AbstractUserRole):
    available_permissions = {
        'cadastrar_porteiro': True,
        'cadastrar_apartamento': True,
        'cadastrar_morador': True,
        'cadastrar_carro_morador': True,
        'cadastrar_moto_morador': True,
        'visualizar_visitante': True,
        'visualizar_carro_visitante': True,
        'visualizar_registro_visitante': True,
        'visualizar_registro_morador': True,
        }

class Porteiro(AbstractUserRole):
    available_permissions = {
        'cadastrar_visitante': True,
        'cadastrar_carro_visitante': True,
        'cadastrar_registro_visitante': True,
        'cadastrar_registro_morador': True,
        'visualizar_morador': True,
        'visualizar_apartamento': True,
        'visualizar_carro_morador': True,
        'visualizar_moto_morador': True,
        }