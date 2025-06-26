import os
os.system("cls")

# Atividade 08
#bibliotecas
import random

#lista
nomes = []

while True:
    print("1- Cadastrar novo nome")
    print("2- Listar todos os nomes")
    print("3- Sortear nome")
    print("4- Sair do programa")
    print("-------------------------")

    opcao = input("Escolha uma opção: ")
    print("-------------------------")

    # Verifica se a opção é válida
    match opcao:
        case "1":
            nome = input("Digite o nome a ser cadastrado: ")
            nomes.append(nome)
            print(f"Nome '{nome}' cadastrado com sucesso.")
            print("-------------------------")



            
        case "2":
            if nomes:
                print("\n--- Lista de Nomes ---")
                for i, nome in enumerate(nomes):
                    print(f"{i + 1}. {nome}")
            else:
                print("A lista está vazia.")
                print("Por favor, cadastre um nome primeiro.")
                print("-------------------------")


        case "3":
            if nomes:
                nome_sorteado = random.choice(nomes)
                print(f"Nome sorteado: {nome_sorteado}")
            else:
                print("A lista está vazia.")
                print("Por favor, cadastre um nome primeiro.")
            print("-------------------------")

        case "4":
            print("Encerrando o programa.")
            break



        case _:
            print("Opção inválida. Tente novamente.")
            print("-------------------------")




            # Fim do programa




