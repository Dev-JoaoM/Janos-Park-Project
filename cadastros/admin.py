from django.contrib import admin
from .models import Funcionario


class FuncionarioAdmin(admin.ModelAdmin):
    readonly_fields = ("criador_por", )

    def save_model(self, request, obj, form, change):
        usuario = request.user
        obj.registrado_por = usuario
        super(FuncionarioAdmin, self).save_model(request, obj, form, change)

admin.site.register(Funcionario, FuncionarioAdmin)