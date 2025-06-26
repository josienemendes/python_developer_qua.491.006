import os
os.system("cls")
# Atividade 09
# Programa para gerenciar uma lista de nomes
nomes = []

def mostrar_menu():
    print("\n=== MENU ===")
    print("1. Adicionar nome")
    print("2. Listar nomes (em ordem alfabética)")
    print("3. Remover nome")
    print("4. Sair")

def adicionar_nome():
    nome = input("Digite o nome que deseja adicionar: ").strip()
    nomes.append(nome)
    print(f"Nome '{nome}' adicionado com sucesso!")

def listar_nomes():
    if nomes:
        print("\n--- Lista de Nomes (Ordenada) ---")
        for i, nome in enumerate(sorted(nomes), start=1):
            print(f"{i}. {nome}")
    else:
        print("A lista está vazia.")

def remover_nome():
    nome = input("Digite o nome que deseja remover: ").strip()
    if nome in nomes:
        nomes.remove(nome)
        print(f"Nome '{nome}' removido com sucesso.")
    else:
        print(f"Nome '{nome}' não encontrado na lista.")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                adicionar_nome()
            case "2":
                listar_nomes()
            case "3":
                remover_nome()
            case "4":
                print("Encerrando o programa. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
