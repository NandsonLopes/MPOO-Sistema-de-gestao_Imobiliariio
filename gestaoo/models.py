from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.

def validar_cpf(value):
    if len(value) != 11 or not value.isdigit():
        raise ValidationError(_('CPF deve ter 11 dígitos numéricos.'))
    
class Usuario(models.Model):
    nome = models.CharField(max_length=300)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, unique=True, validators=[validar_cpf])

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

    def detalhes_contato(self):
        return f'{self.nome} - {self.email} - {self.telefone}'

class Cliente(Usuario):
    def __str__(self):
        return f'Cliente: {self.nome}'

class AgenteImobiliario(Usuario):
    comissao = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return f'Agente: {self.nome} - Comissão: {self.comissao}%'

    def cadastrarPropriedade(self, endereco, preco):
        propriedade = Propriedade(endereco=endereco, preco=preco)
        propriedade.save()
        return propriedade

    def gerenciarContratos(self, cliente, imovel, data_inicio, data_fim):
        contrato = Contrato(cliente=cliente, imovel=imovel, data_inicio=data_inicio, data_fim=data_fim)
        contrato.save()
        return contrato

    def consultarClientes(self):
        return Cliente.objects.all()

class DonoImovel(Usuario):
    data_aquisicao = models.DateField()

    def __str__(self):
        return f'Dono do Imóvel: {self.nome} - Desde {self.data_aquisicao}'

class Propriedade(models.Model):
    endereco = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    dono = models.OneToOneField(DonoImovel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.endereco} - {self.preco}'

    def calcular_valor_mercado(self):
        return self.preco

class Imovel(Propriedade):
    tamanho = models.FloatField()  # em metros quadrados

    def __str__(self):
        return f'Imóvel: {self.endereco}, {self.tamanho}m²'

    def calcular_valor_mercado(self):
        return self.preco * (self.tamanho / 100) 

class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f'Contrato de {self.cliente} com {self.imovel}'

class Visita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    data_visita = models.DateTimeField()

    def __str__(self):
        return f'Visita de {self.cliente} ao imóvel {self.imovel} em {self.data_visita}'

class Avaliacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    nota = models.IntegerField()  # 1 a 5

    def __str__(self):
        return f'Avaliação de {self.nota} para {self.imovel} por {self.cliente}'

class Documento(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    nome_arquivo = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to='documentos/')

    def __str__(self):
        return f'Documento: {self.nome_arquivo} para o imóvel {self.imovel}'

class Pagamento(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    metodo_pagamento = models.CharField(max_length=50)

    def __str__(self):
        return f'Pagamento de {self.valor} para {self.contrato} em {self.data_pagamento}'
