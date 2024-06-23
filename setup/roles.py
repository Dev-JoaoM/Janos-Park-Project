#import imp
from rolepermissions.roles import AbstractUserRole


class Sindico(AbstractUserRole):
    available_permissions = {
        'cadastrar_adm': True,
        'cadastrar_porteiro': True,
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


class Administrador(AbstractUserRole):
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