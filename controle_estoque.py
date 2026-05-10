# Importa datetime para marcação de hora nas movimentações
from datetime import datetime

# Variáveis Globais
estoque = [
    {"id": 1, "nome": "Papel Sulfite (Resma)", "quantidade": 0},
    {"id": 2, "nome": "Envelope A4", "quantidade": 0},
    {"id": 3, "nome": "Caneta Esferográfica (Azul)", "quantidade": 0},
    {"id": 4, "nome": "Caneta Esferográfica (Preta)", "quantidade": 0},
    {"id": 5, "nome": "Elástico (Pacote 50un)", "quantidade": 0},
    {"id": 6, "nome": "Fita Adesiva", "quantidade": 0}
]
movimentacoes = []
responsavel = ""

# Funcionalidades
def eh_numero(valor):
    try:
        numero = int(valor)
        return True
    except ValueError:
        print("Valor inválido. Tente novamente.\n")
        return False

def login():
    print("-----------------------------")
    print("----------- LOGIN -----------")
    usuario = input("Usuário: ")
    return usuario

def registrar_movimentacao(operacao, id, quantidade):
    movimentacao = {
        "id": len(movimentacoes),
        "data_hora": datetime.now(),
        "operacao": operacao,
        "responsavel": responsavel,
        "id_produto": id,
        "quantidade": quantidade
    }
    movimentacoes.append(movimentacao)

def adicionar_produto():
    consultar_estoque()
    print("-----------------------------")
    print("----- ADICIONAR PRODUTO -----")
    teste = False
    while teste == False:
        id = input("Informe o código do produto: ")
        teste = eh_numero(id)
    id = int(id)
    teste = False
    while teste == False:
        quantidade = input("Informe a quantidade a ser adicionada: ")
        teste = eh_numero(quantidade)
    quantidade = int(quantidade)
    mensagem = "{} unidades de {} adicionadas.\n"
    for produto in estoque:
        if produto["id"] == id:
            produto["quantidade"] += quantidade
            registrar_movimentacao("entrada", id, quantidade)
            print(mensagem.format(quantidade, produto["nome"]))
            return
    
def remover_produto():
    consultar_estoque()
    print("-----------------------------")
    print("------ REMOVER PRODUTO ------")
    id = int(input("Informe o código do produto: "))
    quantidade = int(input("Informe a quantidade a ser retirada: "))
    mensagem = "{} unidades de {} retiradas.\n"
    for produto in estoque:
        if produto["id"] == id:
            if produto["quantidade"] < quantidade:
                print("Erro: Quantidade de retirada excede estoque.\n")
                return
            produto["quantidade"] -= quantidade
            registrar_movimentacao("saida", id, quantidade)
            print(mensagem.format(quantidade, produto["nome"]))
            return

def consultar_estoque():
    mensagem = "ID: {} | Produto: {} | Estoque: {}"
    
    for produto in estoque:
        print(mensagem.format(str(produto["id"]).rjust(2), produto["nome"].ljust(30), produto["quantidade"]))

def consultar_movimentacoes():
    if len(movimentacoes) == 0:
        print("Sem movimentações registradas.\n")
        return
    mensagem = "{} | Usuário {} {} {} unidade(s) de {}."
    for movimentacao in movimentacoes:
        operacao = "adicionou" if movimentacao["operacao"] == "entrada" else "removeu"
        for produto in estoque:
            if produto["id"] == movimentacao["id_produto"]:
                nome_produto = produto["nome"]
                break
        print(mensagem.format(movimentacao["data_hora"], movimentacao["responsavel"], operacao, movimentacao["quantidade"], nome_produto))



# Rotina Principal
print("Controle de Estoque do Daniel Silvente Pereira")

# Login/Identificação de Responsável
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
