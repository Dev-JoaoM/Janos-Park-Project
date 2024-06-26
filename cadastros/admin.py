from django.contrib import admin
from .models import RegistroVisitante
from django.contrib.auth import admin as admin_auth_django


"""class FuncionarioAdmin(admin.ModelAdmin):
    readonly_fields = ("criador_por", )

    def save_model(self, request, obj, form, change):
        usuario = request.user
        obj.registrado_por = usuario
        super(FuncionarioAdmin, self).save_model(request, obj, form, change)

admin.site.register(Funcionario, FuncionarioAdmin)"""


#@admin.register(RegistroVisitante)
class RegistroVisitanteAdmin(admin.ModelAdmin):
    model = RegistroVisitante
    readonly_fields = ("data_entrada", "data_saida" )
    #fieldsets =fields + (
      #  ('Informações de Registro', {'fields': ("visitante", "morador", "autorizacao", "data_entrada")}),)
    
    """def save_model(self, request, obj, form, change):
        usuario = request.user
        obj.data_entrada = usuario
        super(RegistroVisitanteAdmin, self).save_model(request, obj, form, change)"""

admin.site.register(RegistroVisitante, RegistroVisitanteAdmin)