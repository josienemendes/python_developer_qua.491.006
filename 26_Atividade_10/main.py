
import os
os.system("cls")
# Atividade 10
# Programa para gerenciar uma lista de números inteiros
numeros = []

def mostrar_menu():
    print("\n=== MENU ===")
    print("1. Adicionar número")
    print("2. Listar números (ordem crescente)")
    print("3. Remover número")
    print("4. Mostrar estatísticas (média, maior, menor)")
    print("5. Sair")

def adicionar_numero():
    try:
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
        print(f"Número {numero} adicionado com sucesso!")
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")

def listar_numeros():
    if numeros:
        print("\n--- Números em ordem crescente ---")
        for i, num in enumerate(sorted(numeros), start=1):
            print(f"{i}. {num}")
    else:
        print("A lista está vazia.")

def remover_numero():
    try:
        numero = int(input("Digite o número que deseja remover: "))
        if numero in numeros:
            numeros.remove(numero)
            print(f"Número {numero} removido com sucesso.")
        else:
            print("Número não encontrado na lista.")
    except ValueError:
        print("Digite um número inteiro válido.")

def mostrar_estatisticas():
    if numeros:
        media = sum(numeros) / len(numeros)
        maior = max(numeros)
        menor = min(numeros)
        print(f"\nEstatísticas:")
        print(f"- Média: {media:.2f}")
        print(f"- Maior número: {maior}")
        print(f"- Menor número: {menor}")
    else:
        print("A lista está vazia.")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                adicionar_numero()
            case "2":
                listar_numeros()
            case "3":
                remover_numero()
            case "4":
                mostrar_estatisticas()
            case "5":
                print("Encerrando o programa. Até mais!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
