import os
os.system("cls")

# Lista principal
nomes = []

# Função para cadastrar um nome
def cadastrar_nome():
    nome = input("Digite o nome para cadastrar: ")
    nomes.append(nome)
    print(f"Nome '{nome}' cadastrado com sucesso!")

# Função para listar os nomes
def listar_nomes():
    if nomes:
        print("\n--- Lista de Nomes ---")
        for i, nome in enumerate(nomes, start=1):
            print(f"{i}. {nome}")
    else:
        print("A lista está vazia.")

# Função para pesquisar nome
def pesquisar_nome():
    nome = input("Digite o nome para pesquisar: ")
    if nome in nomes:
        print(f"Nome '{nome}' encontrado!")
    else:
        print(f"Nome '{nome}' não encontrado.")

# Função para alterar nome
def alterar_nome():
    antigo = input("Digite o nome que deseja alterar: ")
    if antigo in nomes:
        novo = input("Digite o novo nome: ")
        posicao = nomes.index(antigo)
        nomes[posicao] = novo
        print(f"Nome '{antigo}' alterado para '{novo}'.")
    else:
        print(f"Nome '{antigo}' não encontrado.")

# Função para excluir nome
def excluir_nome():
    nome = input("Digite o nome que deseja excluir: ")
    if nome in nomes:
        nomes.remove(nome)
        print(f"Nome '{nome}' excluído com sucesso.")
    else:
        print(f"Nome '{nome}' não encontrado.")

# Função principal
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar nome")
        print("2. Listar nomes")
        print("3. Pesquisar nome")
        print("4. Alterar nome")
        print("5. Excluir nome")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_nome()
        elif escolha == '2':
            listar_nomes()
        elif escolha == '3':
            pesquisar_nome()
        elif escolha == '4':
            alterar_nome()
        elif escolha == '5':
            excluir_nome()
        elif escolha == '6':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
menu()
