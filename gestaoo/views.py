from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, AgenteImobiliario, DonoImovel, Propriedade, Imovel, Contrato, Visita, Avaliacao, Documento, Pagamento

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'imobiliaria/clientes_list.html', {'clientes': clientes})

def detalhe_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'imobiliaria/cliente_detalhes.html', {'cliente': cliente})

def criar_cliente(request):
    if request.method == 'POST':
        cliente = Cliente(
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            telefone=request.POST.get('telefone'),
            cpf=request.POST.get('cpf')
        )
        cliente.save()
        return redirect('listar_clientes')
    return render(request, 'imobiliaria/cliente_form.html')

def listar_agentes(request):
    agentes = AgenteImobiliario.objects.all()
    return render(request, 'imobiliaria/agentes_list.html', {'agentes': agentes})

def detalhe_agente(request, pk):
    agente = get_object_or_404(AgenteImobiliario, pk=pk)
    clientes = agente.consultarClientes()  # Usando o método da classe
    return render(request, 'imobiliaria/agente_detalhes.html', {'agente': agente, 'clientes': clientes})

def criar_agente(request):
    if request.method == 'POST':
        agente = AgenteImobiliario(
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            telefone=request.POST.get('telefone'),
            cpf=request.POST.get('cpf'),
            comissao=request.POST.get('comissao')
        )
        agente.save()
        return redirect('listar_agentes')
    return render(request, 'imobiliaria/agente_form.html')

def listar_donos_imoveis(request):
    donos = DonoImovel.objects.all()
    return render(request, 'imobiliaria/donos_imoveis_list.html', {'donos': donos})

def detalhe_dono(request, pk):
    dono = get_object_or_404(DonoImovel, pk=pk)
    return render(request, 'imobiliaria/dono_detalhes.html', {'dono': dono})

def criar_dono(request):
    if request.method == 'POST':
        dono = DonoImovel(
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            telefone=request.POST.get('telefone'),
            cpf=request.POST.get('cpf'),
            data_aquisicao=request.POST.get('data_aquisicao')
        )
        dono.save()
        return redirect('listar_donos_imoveis')
    return render(request, 'imobiliaria/dono_form.html')

def listar_propriedades(request):
    propriedades = Propriedade.objects.all()
    return render(request, 'imobiliaria/propriedades_list.html', {'propriedades': propriedades})

def detalhe_propriedade(request, pk):
    propriedade = get_object_or_404(Propriedade, pk=pk)
    return render(request, 'imobiliaria/propriedade_detalhes.html', {'propriedade': propriedade})

def criar_propriedade(request):
    if request.method == 'POST':
        propriedade = Propriedade(
            endereco=request.POST.get('endereco'),
            preco=request.POST.get('preco'),
            dono=get_object_or_404(DonoImovel, pk=request.POST.get('dono'))
        )
        propriedade.save()
        return redirect('listar_propriedades')
    return render(request, 'imobiliaria/propriedade_form.html')

def listar_imoveis(request):
    imoveis = Imovel.objects.all()
    return render(request, 'imobiliaria/imoveis_list.html', {'imoveis': imoveis})

def detalhe_imovel(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)
    return render(request, 'imobiliaria/imovel_detalhes.html', {'imovel': imovel})

def criar_imovel(request):
    if request.method == 'POST':
        imovel = Imovel(
            endereco=request.POST.get('endereco'),
            preco=request.POST.get('preco'),
            tamanho=request.POST.get('tamanho'),
            dono=get_object_or_404(DonoImovel, pk=request.POST.get('dono'))
        )
        imovel.save()
        return redirect('listar_imoveis')
    return render(request, 'imobiliaria/imovel_form.html')

def listar_contratos(request):
    contratos = Contrato.objects.all()
    return render(request, 'imobiliaria/contratos_list.html', {'contratos': contratos})

def detalhe_contrato(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    return render(request, 'imobiliaria/contrato_detalhes.html', {'contrato': contrato})

def criar_contrato(request):
    if request.method == 'POST':
        contrato = Contrato(
            cliente=get_object_or_404(Cliente, pk=request.POST.get('cliente')),
            imovel=get_object_or_404(Imovel, pk=request.POST.get('imovel')),
            data_inicio=request.POST.get('data_inicio'),
            data_fim=request.POST.get('data_fim')
        )
        contrato.save()
        return redirect('listar_contratos')
    return render(request, 'imobiliaria/contrato_form.html')

def listar_visitas(request):
    visitas = Visita.objects.all()
    return render(request, 'imobiliaria/visitas_list.html', {'visitas': visitas})

def detalhe_visita(request, pk):
    visita = get_object_or_404(Visita, pk=pk)
    return render(request, 'imobiliaria/visita_detalhes.html', {'visita': visita})

def criar_visita(request):
    if request.method == 'POST':
        visita = Visita(
            cliente=get_object_or_404(Cliente, pk=request.POST.get('cliente')),
            imovel=get_object_or_404(Imovel, pk=request.POST.get('imovel')),
            data_visita=request.POST.get('data_visita')
        )
        visita.save()
        return redirect('listar_visitas')
    return render(request, 'imobiliaria/visita_form.html')

def listar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    return render(request, 'imobiliaria/avaliacoes_list.html', {'avaliacoes': avaliacoes})

def detalhe_avaliacao(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    return render(request, 'imobiliaria/avaliacao_detalhes.html', {'avaliacao': avaliacao})

def criar_avaliacao(request):
    if request.method == 'POST':
        avaliacao = Avaliacao(
            cliente=get_object_or_404(Cliente, pk=request.POST.get('cliente')),
            imovel=get_object_or_404(Imovel, pk=request.POST.get('imovel')),
            nota=request.POST.get('nota')
        )
        avaliacao.save()
        return redirect('listar_avaliacoes')
    return render(request, 'imobiliaria/avaliacao_form.html')

def listar_documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'imobiliaria/documentos_list.html', {'documentos': documentos})

def detalhe_documento(request, pk):
    documento = get_object_or_404(Documento, pk=pk)
    return render(request, 'imobiliaria/documento_detalhes.html', {'documento': documento})

def criar_documento(request):
    if request.method == 'POST':
        documento = Documento(
            imovel=get_object_or_404(Imovel, pk=request.POST.get('imovel')),
            nome_arquivo=request.POST.get('nome_arquivo'),
            arquivo=request.FILES.get('arquivo')
        )
        documento.save()
        return redirect('listar_documentos')
    return render(request, 'imobiliaria/documento_form.html')

def listar_pagamentos(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'imobiliaria/pagamentos_list.html', {'pagamentos': pagamentos})

def detalhe_pagamento(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    return render(request, 'imobiliaria/pagamento_detalhes.html', {'pagamento': pagamento})
