import os
os.system("cls")

""""
# Atividade 07
#TODO: Crie um programa que faça as seguintes operações:

-Cadastre novo nome na lista
-Liste todos os nomes na lista
-Pesquise por nome na lista
-Altere um nome na lista
-Exclua um nome na lista
-Sair do programa
#NOTE: a lista deve começar vazia. exemplo : list = []
"""
def menu():
    print("\n=== MENU ===")
    print("1. Cadastrar novo nome")
    print("2. Listar todos os nomes")
    print("3. Pesquisar por nome")
    print("4. Alterar um nome")
    print("5. Excluir um nome")
    print("6. Sair")


def main():
    lista = []

    while True:
        menu()
        opcao = input("Escolha uma opção (1-6): ")

        if opcao == '1':
            nome = input("Digite o nome a ser cadastrado: ").strip()
            lista.append(nome)
            print(f"Nome '{nome}' cadastrado com sucesso.")

        elif opcao == '2':
            if lista:
                print("\n--- Lista de Nomes ---")
                for i, nome in enumerate(lista):
                    print(f"{i + 1}. {nome}")
            else:
                print("A lista está vazia.")

        elif opcao == '3':
            nome_pesquisa = input("Digite o nome a ser pesquisado: ").strip()
            if nome_pesquisa in lista:
                print(f"Nome '{nome_pesquisa}' encontrado na lista.")
            else:
                print(f"Nome '{nome_pesquisa}' não encontrado.")

        elif opcao == '4':
            nome_antigo = input("Digite o nome que deseja alterar: ").strip()
            if nome_antigo in lista:
                novo_nome = input("Digite o novo nome: ").strip()
                index = lista.index(nome_antigo)
                lista[index] = novo_nome
                print(f"Nome '{nome_antigo}' alterado para '{novo_nome}'.")
            else:
                print(f"Nome '{nome_antigo}' não encontrado na lista.")

        elif opcao == '5':
            nome_excluir = input("Digite o nome que deseja excluir: ").strip()
            if nome_excluir in lista:
                lista.remove(nome_excluir)
                print(f"Nome '{nome_excluir}' excluído com sucesso.")
            else:
                print(f"Nome '{nome_excluir}' não encontrado na lista.")

        elif opcao == '6':
            print("Encerrando o programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

