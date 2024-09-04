# MPOO-Sistema-de-gestao_Imobiliariio
Projeto desenvolvido para a disciplina de MPOO do Curso  de sistemas de Informação da UFRPE-UAST. Discente: Nandson Raynan C. Lopes
Documentação do Sistema de Gestão Imobiliária
Visão Geral
O sistema de gestão imobiliária é uma aplicaçã desenvolvida com Django para gerenciar propriedades, imóveis, clientes, agentes imobiliários, contratos, visitas, avaliações, documentos e pagamentos. O projeto utiliza os conceitos de Programação Orientada a Objetos (POO), para estruturar o código de maneira eficiente.
Requisitos
⦁	Python 3.7+
⦁	Django 4.0+
⦁	Bibliotecas Adicionais:
Configuração do Ambiente windows
1. Baixar o Instalador do Python:
⦁	Acesse o site oficial do Python.
⦁	Baixe o instalador da versão mais recente do Python 3.x para Windows.
2. Executar o Instalador:
⦁	Execute o instalador baixado.
⦁	Importante: Marque a opção "Add Python to PATH" antes de clicar em "Install Now".
⦁	Clique em "Install Now" e siga as instruções para concluir a instalação.
 3. Criar e Ativar um Ambiente Virtual
⦁	Navegue até o diretório onde você deseja criar o ambiente virtual.
⦁	Execute o comando para criar um ambiente virtual:
python -m venv venv
⦁	Execute o comando para ativar o ambiente virtual
venv\Scripts\activate
⦁	Você deve ver (venv) antes do prompt de comando indicando que o ambiente virtual está ativado.
4. Instalar o Django:
⦁	Com o ambiente virtual ativado, execute o comando:
pip install django
⦁	Para verificar se o Django foi instalado corretamente, execute:
python -m django --version
5. Criar novo projeto Django
django-admin startproject nome_do_projeto
6. Iniciar servidor de desenvolvimento
python manage.py runserver
Descrição dos Modelos
1. Cliente
⦁	nome: Nome do cliente
⦁	email: E-mail do cliente
⦁	telefone: Telefone do cliente
⦁	cpf: CPF do cliente
2. AgenteImobiliario
⦁	nome: Nome do agente
⦁	email: E-mail do agente
⦁	telefone: Telefone do agente
⦁	cpf: CPF do agente
⦁	comissao: Comissão do agente
3. DonoImovel
⦁	nome: Nome do dono
⦁	email: E-mail do dono
⦁	telefone: Telefone do dono
⦁	cpf: CPF do dono
⦁	data_aquisicao: Data de aquisição do imóvel
4. Propriedade
⦁	endereco: Endereço da propriedade
⦁	preco: Preço da propriedade
⦁	dono: Relacionamento com DonoImovel
5. Imovel
⦁	endereco: Endereço do imóvel
⦁	preco: Preço do imóvel
⦁	tamanho: Tamanho do imóvel
⦁	dono: Relacionamento com DonoImovel
6. Contrato
⦁	cliente: Relacionamento com Cliente
⦁	imovel: Relacionamento com Imovel
⦁	data_inicio: Data de início do contrato
⦁	data_fim: Data de fim do contrato
7. Visita
⦁	cliente: Relacionamento com Cliente
⦁	imovel: Relacionamento com Imovel
⦁	data_visita: Data da visita
8. Avaliacao
⦁	cliente: Relacionamento com Cliente
⦁	imovel: Relacionamento com Imovel
⦁	nota: Nota da avaliação
9. Documento
⦁	imovel: Relacionamento com Imovel
⦁	nome_arquivo: Nome do arquivo
⦁	arquivo: Arquivo em si
10. Pagamento
⦁	contrato: Relacionamento com Contrato
⦁	valor: Valor do pagamento
⦁	data_pagamento: Data do pagamento
Views
As views no Django são responsáveis por processar as solicitações HTTP e retornar as respostas apropriadas. As principais views implementadas são:
⦁	Listar: Para listar todos os registros de um determinado modelo.
⦁	Detalhes: Para exibir detalhes de um registro específico.
⦁	Criar: Para criar novos registros.
Cada view segue uma estrutura simples, verificando o método da solicitação e manipulando os dados conforme necessário. 
Testes
Os testes para o projeto devem ser adicionados em tests.py dentro de cada aplicativo. 
Contribuição
Se você deseja contribuir para o projeto, por favor, faça um fork do repositório e envie suas pull requests.
