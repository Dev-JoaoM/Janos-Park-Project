#import imp
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Colaborador
from rolepermissions.roles import assign_role


@receiver(post_save, sender=Colaborador)
def define_permissoes(sender, instance, created, **kwargs):
    if created:
        if instance.cargo == "ADM":
            assign_role(instance, "administrador")
        elif instance.cargo == "PTR":
            assign_role(instance, "porteiro")
        elif instance.cargo == "SDC":
            assign_role(instance, "sindico")