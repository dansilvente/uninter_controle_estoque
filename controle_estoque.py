# História de Usuário: Entrada de Produto no Estoque
# Um funcionário do setor de almoxarifado precisa registrar a entrada de produtos no estoque,
# para que o sistema reflita corretamente os itens disponíveis após uma nova entrega ou compra.
# Critérios de Aceitação são:
# • O sistema deve permitir selecionar um produto já cadastrado.
# • Deve ser possível informar a quantidade recebida e a data da entrada.
# • O estoque do produto deve ser atualizado automaticamente.
# Além disso, precisará adicionar neste sistema algumas funcionalidades para ajudar na distribuição de materiais para registrar a saída de produtos do estoque mantendo o controle preciso dos
# itens utilizados ou entregues.
# Critérios de Aceitação:
# • O sistema deve permitir selecionar um produto e informar a quantidade retirada.
# • Deve validar se há quantidade suficiente no estoque antes de confirmar a saída.
# • O sistema deve registrar a movimentação com data e responsável.

# LOGIN
# Nome sem espaços - Senha igual o nome
def login():
    print("-----------------------------")
    print("----------- LOGIN -----------")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if (usuario == senha):
        print("Login com sucesso.")
        return usuario
    print("Credenciais inválidas.")
    return ""

def adicionar_produto(responsavel):
    print("-----------------------------")
    print("----- ADICIONAR PRODUTO -----")
    id = input("Informe o código do produto, caso exista: ")
    if (id == "")
    nome = input("Digite o nome do produto: ")
    quantidade = input("Informe a quantidade a ser adicionada: ") 
    entrada = {
        "id": str(id),
        "nome": nome,
        "quantidade": quantidade,
        "responsavel": responsavel
    }
    estoque.adicionar(entrada)
    print("------------------------------\n")
    
def remover_produto():
    ""

def consultar_estoque():
    ""

def consultar_movimentacoes():
    ""

def verificar_id(id):
    for produto in estoque:
        if (id == produto["id"]):
            return True
    return False

# Variáveis Globais
estoque = []
movimentacoes = []
responsavel = ""

# Início
print("Controle de Estoque do Daniel Silvente Pereira")

while responsavel == "":
    responsavel = login()

# Menu Principal
opcao_selecionada = ""
while not opcao_selecionada == "5":
    print("------------------------------")
    print("------- MENU PRINCIPAL -------")
    print("Escolha a opção desejada:")
    print("1 - Adicionar Produto")
    print("2 - Remover Produto")
    print("3 - Consultar Estoque")
    print("4 - Consultar Movimentações")
    print("5 - Encerrar Programa")
    opcao_selecionada = input(">>")

    match opcao_selecionada:
        # Adicionar Produto
        case "1":
            adicionar_produto()
        # Remover Produto
        case "2":
            remover_produto()
        # Consultar Estoque
        case "3":
            consultar_estoque()
        case "4":
            consultar_movimentacoes()
        # Encerrar o Programa
        case "5":
            break
        # Opção Inválida
        case _:
            print("Opção inválida")
