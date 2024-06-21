import imp
from django.dispatch import receiver
from django.db.models.signals import post_save
#from .models import Users
from .models import Colaborador
from rolepermissions.roles import assign_role

"""@receiver(post_save, sender=Users)
def define_permissoes(sender, instance, created, **kwargs):
    if created:
        if instance.cargo == "V":
            assign_role(instance, 'vendedor')
        elif instance.cargo == "G":
            assign_role(instance, 'gerente')"""


@receiver(post_save, sender=Colaborador)
def define_permissoes(sender, instance, created, **kwargs):
    if created:
        if instance.cargo == "ADM":
            assign_role(instance, "Administrador(a)")
        elif instance.cargo == "PTR":
            assign_role(instance, "Porteiro(a)")
        elif instance.cargo == "SDC":
            assign_role(instance, "Síndico(a)")
