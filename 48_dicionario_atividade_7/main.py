""" Crie um programa de loja de roupa simples usando dicionário """

# Loja de roupa simples usando dicionário e match-case no menu

estoque = {}  # Dicionário para armazenar as roupas, chave será o código da roupa

def adicionar_roupa():
    codigo = input("Código da roupa: ").strip()  # Pede o código da roupa
    if codigo in estoque:  # Verifica se código já existe
        print("Código já existe no estoque.\n")
        return  # Sai da função para evitar sobrescrever

    nome = input("Nome da roupa: ").strip()  # Nome da peça
    tamanho = input("Tamanho (P, M, G, GG): ").strip().upper()  # Tamanho convertido para maiúsculo
    try:
        preco = float(input("Preço: R$ ").replace(',', '.'))  # Preço convertido para float (aceita vírgula)
        quantidade = int(input("Quantidade: "))  # Quantidade em estoque (inteiro)
        if preco < 0 or quantidade < 0:  # Verifica se valores são positivos
            print("Preço e quantidade devem ser positivos.\n")
            return
    except ValueError:  # Caso não seja possível converter para float ou int
        print("Valor inválido para preço ou quantidade.\n")
        return

    # Adiciona o produto no dicionário com o código como chave e um dicionário com os dados como valor
    estoque[codigo] = {
        "nome": nome,
        "tamanho": tamanho,
        "preco": preco,
        "quantidade": quantidade
    }
    print(f"Roupa '{nome}' adicionada ao estoque.\n")  # Confirmação

def listar_roupas():
    if not estoque:  # Se o estoque estiver vazio
        print("Estoque vazio.\n")
        return

    print("\n--- ROUPAS NO ESTOQUE ---")
    # Percorre todas as roupas no estoque e imprime os detalhes
    for cod, dados in estoque.items():
        print(f"Código: {cod} | {dados['nome']} | Tamanho: {dados['tamanho']} | Preço: R$ {dados['preco']:.2f} | Quantidade: {dados['quantidade']}")
    print()

def vender_roupa():
    codigo = input("Código da roupa para vender: ").strip()  # Código do produto para vender
    if codigo not in estoque:  # Verifica se o código existe
        print("Roupa não encontrada.\n")
        return

    try:
        qtd_venda = int(input("Quantidade para vender: "))  # Quantidade desejada para venda
        if qtd_venda <= 0:
            print("Quantidade deve ser maior que zero.\n")
            return
    except ValueError:  # Caso valor digitado não seja inteiro
        print("Quantidade inválida.\n")
        return

    if estoque[codigo]["quantidade"] < qtd_venda:  # Verifica estoque suficiente
        print("Quantidade insuficiente em estoque.\n")
        return

    # Deduz a quantidade vendida do estoque
    estoque[codigo]["quantidade"] -= qtd_venda
    total = qtd_venda * estoque[codigo]["preco"]  # Calcula o valor total da venda
    print(f"Venda realizada: {qtd_venda}x {estoque[codigo]['nome']} - Total: R$ {total:.2f}\n")

    # Se a quantidade chegar a zero, remove o produto do estoque
    if estoque[codigo]["quantidade"] == 0:
        print("Estoque zerado, removendo roupa do sistema.")
        del estoque[codigo]

def remover_roupa():
    codigo = input("Código da roupa para remover: ").strip()  # Código para remover
    if codigo in estoque:  # Verifica se existe
        del estoque[codigo]  # Remove do dicionário
        print("Roupa removida do estoque.\n")
    else:
        print("Roupa não encontrada.\n")

def menu():
    while True:
        print("=== LOJA DE ROUPAS ===")
        print("1. Adicionar roupa")
        print("2. Listar roupas")
        print("3. Vender roupa")
        print("4. Remover roupa")
        print("5. Sair")

        escolha = input("Escolha uma opção: ").strip()  # Pede opção do usuário

        # Usando match-case para tratar as opções do menu
        match escolha:
            case '1':
                adicionar_roupa()  # Chama função para adicionar roupa
            case '2':
                listar_roupas()  # Chama função para listar roupas
            case '3':
                vender_roupa()  # Chama função para vender roupa
            case '4':
                remover_roupa()  # Chama função para remover roupa
            case '5':
                print("Encerrando sistema da loja.")  # Mensagem de saída
                break  # Sai do loop e encerra o programa
            case _:  # Caso o usuário digite algo diferente das opções válidas
                print("Opção inválida.\n")

menu()  # Inicia o programa executando o menu
