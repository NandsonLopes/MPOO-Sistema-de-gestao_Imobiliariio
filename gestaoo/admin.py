from django.contrib import admin
from .models import Cliente, AgenteImobiliario, DonoImovel, Propriedade, Imovel, Contrato, Visita, Avaliacao, Documento, Pagamento

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cpf')
    search_fields = ('nome', 'cpf')

class AgenteImobiliarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'comissao')
    search_fields = ('nome', 'cpf')

class DonoImovelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_aquisicao')
    search_fields = ('nome', 'cpf')

class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'preco', 'dono')
    search_fields = ('endereco',)
    list_filter = ('dono',)

class ImovelAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'preco', 'tamanho', 'dono')
    search_fields = ('endereco',)
    list_filter = ('dono',)

class ContratoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'imovel', 'data_inicio', 'data_fim')
    search_fields = ('cliente__nome',)
    list_filter = ('data_inicio',)

class VisitaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'imovel', 'data_visita')
    search_fields = ('cliente__nome',)

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'imovel', 'nota')
    search_fields = ('cliente__nome',)

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('nome_arquivo', 'imovel')
    search_fields = ('nome_arquivo',)

class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'valor', 'data_pagamento', 'metodo_pagamento')
    search_fields = ('contrato__cliente__nome',)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(AgenteImobiliario, AgenteImobiliarioAdmin)
admin.site.register(DonoImovel, DonoImovelAdmin)
admin.site.register(Propriedade, PropriedadeAdmin)
admin.site.register(Imovel, ImovelAdmin)
admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Visita, VisitaAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Pagamento, PagamentoAdmin)
