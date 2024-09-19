from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime

def validar_cpf(value):
    if len(value) != 11 or not value.isdigit():
        raise ValidationError(_('CPF deve ter 11 dígitos numéricos.'))

class Usuario(models.Model):
    nome = models.CharField(max_length=300)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, unique=True, validators=[validar_cpf])
    data_nascimento = models.DateField(null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

    def detalhes_contato(self):
        return f'{self.nome} - {self.email} - {self.telefone}'

    def tem_contratos_ativos(self):
        return self.contratos.filter(data_fim__gte=datetime.date.today()).exists()

class Cliente(Usuario):
    def __str__(self):
        return f'Cliente: {self.nome}'

class AgenteImobiliario(Usuario):
    comissao = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return f'Agente: {self.nome} - Comissão: {self.comissao}%'

    def cadastrar_propriedade(self, endereco, preco):
        propriedade = Propriedade(endereco=endereco, preco=preco)
        propriedade.save()
        return propriedade

    def gerenciar_contratos(self, cliente, imovel, data_inicio, data_fim):
        if data_inicio >= data_fim:
            raise ValidationError(_('A data de fim deve ser posterior à data de início.'))
        contrato = Contrato(cliente=cliente, imovel=imovel, data_inicio=data_inicio, data_fim=data_fim)
        contrato.save()
        return contrato

    def consultar_clientes(self):
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
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Imóvel: {self.endereco}, {self.tamanho}m²'

    def calcular_valor_mercado(self):
        return self.preco * (self.tamanho / 100)

    def calcular_roi(self, custo_adicional):
        return (self.preco - custo_adicional) / custo_adicional * 100

class Contrato(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('encerrado', 'Encerrado'),
        ('pendente', 'Pendente'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contratos')
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='contratos')
    data_inicio = models.DateField()
    data_fim = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')

    def __str__(self):
        return f'Contrato de {self.cliente} com {self.imovel}'

    def renovar_contrato(self, nova_data_fim):
        return Contrato.objects.create(cliente=self.cliente, imovel=self.imovel, data_inicio=self.data_fim, data_fim=nova_data_fim)

class Visita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='visitas')
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='visitas')
    data_visita = models.DateTimeField()

    def __str__(self):
        return f'Visita de {self.cliente} ao imóvel {self.imovel} em {self.data_visita}'

class Avaliacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='avaliacoes')
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='avaliacoes')
    nota = models.IntegerField()  # 1 a 5

    def __str__(self):
        return f'Avaliação de {self.nota} para {self.imovel} por {self.cliente}'

class Documento(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='documentos')
    nome_arquivo = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to='documentos/')

    def __str__(self):
        return f'Documento: {self.nome_arquivo} para o imóvel {self.imovel}'

class Pagamento(models.Model):
    STATUS_PAGAMENTO_CHOICES = [
        ('pago', 'Pago'),
        ('pendente', 'Pendente'),
        ('atrasado', 'Atrasado'),
    ]
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='pagamentos')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    metodo_pagamento = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_PAGAMENTO_CHOICES, default='pendente')

    def __str__(self):
        return f'Pagamento de {self.valor} para {self.contrato} em {self.data_pagamento}'

    def esta_atrasado(self):
        return self.data_pagamento < datetime.date.today() and self.status != 'pago'

