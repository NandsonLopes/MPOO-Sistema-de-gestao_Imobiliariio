from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('cliente/<int:pk>/', views.detalhe_cliente, name='detalhe_cliente'),
    path('cliente/criar/', views.criar_cliente, name='criar_cliente'),
    
    path('agentes/', views.listar_agentes, name='listar_agentes'),
    path('agente/<int:pk>/', views.detalhe_agente, name='detalhe_agente'),
    path('agente/criar/', views.criar_agente, name='criar_agente'),

    path('donos/', views.listar_donos_imoveis, name='listar_donos_imoveis'),
    path('dono/<int:pk>/', views.detalhe_dono, name='detalhe_dono'),
    path('dono/criar/', views.criar_dono, name='criar_dono'),

    path('propriedades/', views.listar_propriedades, name='listar_propriedades'),
    path('propriedade/<int:pk>/', views.detalhe_propriedade, name='detalhe_propriedade'),
    path('propriedade/criar/', views.criar_propriedade, name='criar_propriedade'),

    path('imoveis/', views.listar_imoveis, name='listar_imoveis'),
    path('imovel/<int:pk>/', views.detalhe_imovel, name='detalhe_imovel'),
    path('imovel/criar/', views.criar_imovel, name='criar_imovel'),

    path('contratos/', views.listar_contratos, name='listar_contratos'),
    path('contrato/<int:pk>/', views.detalhe_contrato, name='detalhe_contrato'),
    path('contrato/criar/', views.criar_contrato, name='criar_contrato'),
    path('contrato/renovar/<int:pk>/', views.renovar_contrato, name='renovar_contrato'),  # Nova URL para renovação de contrato

    path('visitas/', views.listar_visitas, name='listar_visitas'),
    path('visita/<int:pk>/', views.detalhe_visita, name='detalhe_visita'),
    path('visita/criar/', views.criar_visita, name='criar_visita'),

    path('avaliacoes/', views.listar_avaliacoes, name='listar_avaliacoes'),
    path('avaliacao/<int:pk>/', views.detalhe_avaliacao, name='detalhe_avaliacao'),
    path('avaliacao/criar/', views.criar_avaliacao, name='criar_avaliacao'),

    path('documentos/', views.listar_documentos, name='listar_documentos'),
    path('documento/<int:pk>/', views.detalhe_documento, name='detalhe_documento'),
    path('documento/criar/', views.criar_documento, name='criar_documento'),

    path('pagamentos/', views.listar_pagamentos, name='listar_pagamentos'),
    path('pagamento/<int:pk>/', views.detalhe_pagamento, name='detalhe_pagamento'),
    path('pagamento/criar/', views.criar_pagamento, name='criar_pagamento'),
]

