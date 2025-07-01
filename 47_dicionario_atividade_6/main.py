"""
Crie um programa que

- use  dicionário com IDs automáticos

- Marcação de status booleano (True/False)

- Filtros com base no conteúdo

- Organização de tarefas como em apps tipo Todoist ou Trello

"""

# Sistema de Controle de Tarefas com Dicionário 

tarefas = {}
proximo_id = 1  # ID automático para cada tarefa

# Adicionar nova tarefa
def adicionar_tarefa():
    global proximo_id
    descricao = input("Descrição da tarefa: ").strip()
    if not descricao:
        print("Descrição não pode estar vazia.\n")
        return

    tarefas[proximo_id] = {"descricao": descricao, "concluida": False}
    print(f"Tarefa #{proximo_id} adicionada!\n")
    proximo_id += 1

# Listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return

    print("\n--- TODAS AS TAREFAS ---")
    for id, tarefa in tarefas.items():
        status = "✅ Concluída" if tarefa["concluida"] else "❌ Pendente"
        print(f"{id}: {tarefa['descricao']} - {status}")
    print()

# Marcar uma tarefa como concluída
def concluir_tarefa():
    try:
        id = int(input("ID da tarefa a concluir: "))
        if id in tarefas:
            tarefas[id]["concluida"] = True
            print("Tarefa marcada como concluída.\n")
        else:
            print("Tarefa não encontrada.\n")
    except ValueError:
        print("ID inválido.\n")

# Remover uma tarefa
def remover_tarefa():
    try:
        id = int(input("ID da tarefa a remover: "))
        if id in tarefas:
            del tarefas[id]
            print("Tarefa removida.\n")
        else:
            print("Tarefa não encontrada.\n")
    except ValueError:
        print("ID inválido.\n")

# Listar pendentes ou concluídas
def listar_por_status():
    status = input("Mostrar (p)endentes ou (c)oncluídas? ").strip().lower()
    if status not in ['p', 'c']:
        print("Opção inválida.\n")
        return

    mostrar_concluidas = status == 'c'
    print("\n--- TAREFAS FILTRADAS ---")
    encontrou = False
    for id, tarefa in tarefas.items():
        if tarefa["concluida"] == mostrar_concluidas:
            status_txt = "✅ Concluída" if tarefa["concluida"] else "❌ Pendente"
            print(f"{id}: {tarefa['descricao']} - {status_txt}")
            encontrou = True
    if not encontrou:
        print("Nenhuma tarefa encontrada com esse status.\n")
    else:
        print()

# Menu principal
def menu():
    while True:
        print("=== MENU TAREFAS ===")
        print("1. Adicionar tarefa")
        print("2. Listar todas as tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Listar tarefas por status")
        print("6. Sair")

        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case '1':
                adicionar_tarefa()
            case '2':
                listar_tarefas()
            case '3':
                concluir_tarefa()
            case '4':
                remover_tarefa()
            case '5':
                listar_por_status()
            case '6':
                print("Saindo do gerenciador de tarefas. Até mais!")
                break
            case _:
                print("Opção inválida.\n")

# Iniciar o programa
menu()
