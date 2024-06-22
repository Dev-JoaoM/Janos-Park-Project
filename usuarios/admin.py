#import imp
from django.contrib import admin
#from .models import Users
from .models import Colaborador
from django.contrib.auth import admin as admin_auth_django
from .forms import UserChangeForm, UserCreationForm #forms sobreescritos

"""
@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Cargo', {'fields': ('cargo',)}),
    )

"""

@admin.register(Colaborador)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Colaborador
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Informações Pessoais', {'fields': ("nome", "dt_nasto","doc_rg", "doc_cpf", "telefone", "cargo")}),
	('Situação', {'fields': ("status", "dt_admissao", "dt_demissao", "motivo_demissao")})
    )

