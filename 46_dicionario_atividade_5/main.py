""" 
Crie um programa para 

- Mostrar o cardápio

-Fazer pedidos (cliente escolhe os itens)

-Ver o pedido atual (o que foi pedido e o total)

-Remover itens do pedido

-Fechar conta (exibir total e limpar pedido)

"""


# Sistema de Pedidos em Restaurante

# Cardápio com código, nome e preço
cardapio = {
    "101": {"nome": "Hambúrguer", "preco": 15.00},
    "102": {"nome": "Pizza", "preco": 30.00},
    "103": {"nome": "Suco", "preco": 7.50},
    "104": {"nome": "Refrigerante", "preco": 6.00},
    "105": {"nome": "Sorvete", "preco": 10.00},
}

# Pedido atual (código: quantidade)
pedido = {}

# Mostrar cardápio
def mostrar_cardapio():
    print("\n--- CARDÁPIO ---")
    for codigo, item in cardapio.items():
        print(f"{codigo} | {item['nome']} - R$ {item['preco']:.2f}")
    print()

# Fazer pedido
def fazer_pedido():
    codigo = input("Digite o código do item: ").strip()
    if codigo not in cardapio:
        print("Código inválido.\n")
        return

    try:
        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            raise ValueError
    except ValueError:
        print("Quantidade inválida.\n")
        return

    if codigo in pedido:
        pedido[codigo] += quantidade
    else:
        pedido[codigo] = quantidade

    print(f"{quantidade}x {cardapio[codigo]['nome']} adicionado ao pedido.\n")

# Ver pedido atual
def ver_pedido():
    if not pedido:
        print("Nenhum item no pedido.\n")
        return

    print("\n--- PEDIDO ATUAL ---")
    total = 0
    for codigo, qtd in pedido.items():
        item = cardapio[codigo]
        subtotal = item['preco'] * qtd
        total += subtotal
        print(f"{qtd}x {item['nome']} - R$ {subtotal:.2f}")

    print(f"TOTAL: R$ {total:.2f}\n")

# Remover item do pedido
def remover_item():
    codigo = input("Código do item para remover: ").strip()
    if codigo not in pedido:
        print("Item não está no pedido.\n")
        return

    del pedido[codigo]
    print("Item removido do pedido.\n")

# Fechar conta
def fechar_conta():
    if not pedido:
        print("Nenhum item no pedido.\n")
        return

    ver_pedido()
    confirmar = input("Deseja finalizar o pedido? (s/n): ").strip().lower()
    if confirmar == 's':
        pedido.clear()
        print("Pedido finalizado. Obrigado!\n")
    else:
        print("Conta não finalizada.\n")

# Menu principal
def menu():
    while True:
        print("=== SISTEMA DE PEDIDOS ===")
        print("1. Mostrar cardápio")
        print("2. Fazer pedido")
        print("3. Ver pedido atual")
        print("4. Remover item do pedido")
        print("5. Fechar conta")
        print("6. Sair")

        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case '1':
                mostrar_cardapio()
            case '2':
                fazer_pedido()
            case '3':
                ver_pedido()
            case '4':
                remover_item()
            case '5':
                fechar_conta()
            case '6':
                print("Encerrando sistema de pedidos. Até logo!")
                break
            case _:
                print("Opção inválida.\n")

# Iniciar sistema
menu()
