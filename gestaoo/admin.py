from django.contrib import admin
# Register your models here.
from .models import Cliente, AgenteImobiliario, DonoImovel, Propriedade, Imovel, Contrato, Visita, Avaliacao, Documento, Pagamento

admin.site.register(Cliente)
admin.site.register(AgenteImobiliario)
admin.site.register(DonoImovel)
admin.site.register(Propriedade)
admin.site.register(Imovel)
admin.site.register(Contrato)
admin.site.register(Visita)
admin.site.register(Avaliacao)
admin.site.register(Documento)
admin.site.register(Pagamento)
