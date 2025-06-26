import os
os.system("cls")

while True:
    nome = input("Informe seu nome: ")
    print(f"Seja bem-vindo, {nome}!")

    prosseguir = input("Deseja continuar? (s/n): ").strip().lower()

    match prosseguir:
        case "s":
            os.system("cls")
            continue
        case "n":
            print("Obrigado por usar o programa!")
            break
        case _:
            print("Opção inválida!")
            break
