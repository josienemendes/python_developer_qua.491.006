# Sistema de Controle de Estoque com dicionário

# Dicionário onde cada chave é o código do produto
estoque = {}

# Adicionar novo produto
def adicionar_produto():
    codigo = input("Código do produto: ").strip()
    if codigo in estoque:
        print("Produto já existe.\n")
        return

    nome = input("Nome do produto: ").strip()
    try:
        quantidade = int(input("Quantidade em estoque: "))
        preco = float(input("Preço unitário: "))
    except ValueError:
        print("Erro: quantidade e preço devem ser números.\n")
        return

    estoque[codigo] = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    print(f"Produto '{nome}' adicionado com sucesso!\n")

# Atualizar estoque de produto existente
def atualizar_estoque():
    codigo = input("Código do produto a atualizar: ").strip()
    if codigo not in estoque:
        print("Produto não encontrado.\n")
        return

    try:
        nova_qtd = int(input("Nova quantidade: "))
        estoque[codigo]["quantidade"] = nova_qtd
        print("Quantidade atualizada com sucesso!\n")
    except ValueError:
        print("Quantidade inválida.\n")

# Ver informações de um produto
def ver_produto():
    codigo = input("Código do produto: ").strip()
    if codigo in estoque:
        p = estoque[codigo]
        print(f"\nProduto: {p['nome']}")
        print(f"Quantidade: {p['quantidade']}")
        print(f"Preço unitário: R$ {p['preco']:.2f}\n")
    else:
        print("Produto não encontrado.\n")

# Listar todos os produtos
def listar_produtos():
    if not estoque:
        print("Nenhum produto cadastrado.\n")
        return

    print("\n--- Estoque Atual ---")
    for codigo, info in estoque.items():
        print(f"Código: {codigo} | Nome: {info['nome']} | Quantidade: {info['quantidade']} | Preço: R$ {info['preco']:.2f}")
    print()

# Remover um produto do estoque
def remover_produto():
    codigo = input("Código do produto a remover: ").strip()
    if codigo in estoque:
        confirm = input(f"Remover produto '{estoque[codigo]['nome']}'? (s/n): ").strip().lower()
        if confirm == 's':
            del estoque[codigo]
            print("Produto removido.\n")
        else:
            print("Remoção cancelada.\n")
    else:
        print("Produto não encontrado.\n")

# Menu principal
def menu():
    while True:
        print("=== MENU ESTOQUE ===")
        print("1. Adicionar produto")
        print("2. Atualizar quantidade")
        print("3. Ver produto")
        print("4. Listar todos os produtos")
        print("5. Remover produto")
        print("6. Sair")

        escolha = input("Escolha uma opção: ").strip()

        match escolha:
            case '1':
                adicionar_produto()
            case '2':
                atualizar_estoque()
            case '3':
                ver_produto()
            case '4':
                listar_produtos()
            case '5':
                remover_produto()
            case '6':
                print("Encerrando sistema de estoque.")
                break
            case _:
                print("Opção inválida.\n")

# Iniciar o programa
menu()
