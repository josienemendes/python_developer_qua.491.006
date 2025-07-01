#  Crie um programa para gerenciar contatos

# Contato pré-cadastrado com dados atualizados
contatos = {
    "Josiene Mendes": {
        "telefone": "61 99860-7397",
        "email": "jossymendes@gmail.com"
    }
}

def adicionar_contato():
    nome = input("Digite o nome do contato: ").strip()
    telefone = input("Digite o telefone: ").strip()
    email = input("Digite o e-mail: ").strip()
    contatos[nome] = {
        "telefone": telefone,
        "email": email
    }
    print(f"Contato '{nome}' adicionado com sucesso!\n")

def buscar_contato():
    nome = input("Digite o nome do contato a buscar: ").strip()
    if nome in contatos:
        print(f"\nInformações de {nome}:")
        print(f"Telefone: {contatos[nome]['telefone']}")
        print(f"E-mail: {contatos[nome]['email']}\n")
    else:
        print(f"Contato '{nome}' não encontrado.\n")

def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.\n")
    else:
        print("\nLista de contatos:")
        for nome, info in contatos.items():
            print(f"- {nome}: Tel: {info['telefone']}, Email: {info['email']}")
        print()

def menu():
    while True:
        print("=== Menu ===")
        print("1. Adicionar contato")
        print("2. Buscar contato")
        print("3. Listar contatos")
        print("4. Sair")

        escolha = input("Escolha uma opção: ").strip()

        match escolha:
            case '1':
                adicionar_contato()
            case '2':
                buscar_contato()
            case '3':
                listar_contatos()
            case '4':
                print("Saindo do programa. Até mais!")
                break
            case _:
                print("Opção inválida. Tente novamente.\n")

menu() 
