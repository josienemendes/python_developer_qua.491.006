import os
os.system("cls")

# Gerenciador de Tarefas - Simples, legível e direto (Zen do Python)

tarefas = []

def mostrar_menu():
    print("\n=== MENU ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Sair")

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        print("\n--- Tarefas ---")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def concluir_tarefa():
    listar_tarefas()
    if tarefas:
        try:
            numero = int(input("Digite o número da tarefa concluída: "))
            tarefa = tarefas.pop(numero - 1)
            print(f"Tarefa '{tarefa}' concluída e removida.")
        except (ValueError, IndexError):
            print("Número inválido. Tente novamente.")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
