# Sistema de Notas de Alunos com Dicionário 

alunos = {}

# Cadastrar aluno e suas notas
def cadastrar_aluno():
    nome = input("Nome do aluno: ").strip()
    if nome in alunos:
        print("Aluno já cadastrado.\n")
        return

    try:
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        n3 = float(input("Nota 3: "))
    except ValueError:
        print("Notas inválidas.\n")
        return

    notas = [n1, n2, n3]
    media = sum(notas) / len(notas)
    situacao = "Aprovado" if media >= 7 else "Reprovado"

    alunos[nome] = {
        "notas": notas,
        "media": media,
        "situacao": situacao
    }
    print(f"Aluno '{nome}' cadastrado com média {media:.2f} - {situacao}\n") 

# Ver dados de um aluno
def ver_aluno():
    nome = input("Nome do aluno: ").strip()
    if nome in alunos:
        dados = alunos[nome]
        print(f"\nAluno: {nome}")
        print(f"Notas: {dados['notas']}")
        print(f"Média: {dados['media']:.2f}")
        print(f"Situação: {dados['situacao']}\n")
    else:
        print("Aluno não encontrado.\n")

# Listar todos os alunos
def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    print("\n--- Lista de Alunos ---")
    for nome, dados in alunos.items():
        print(f"{nome} | Média: {dados['media']:.2f} | Situação: {dados['situacao']}")
    print()

# Remover aluno
def remover_aluno():
    nome = input("Nome do aluno a remover: ").strip()
    if nome in alunos:
        confirmar = input(f"Remover {nome}? (s/n): ").strip().lower()
        if confirmar == 's':
            del alunos[nome]
            print("Aluno removido.\n")
        else:
            print("Remoção cancelada.\n")
    else:
        print("Aluno não encontrado.\n")

# Menu principal
def menu():
    while True:
        print("=== MENU NOTAS ===")
        print("1. Cadastrar aluno")
        print("2. Ver aluno")
        print("3. Listar alunos")
        print("4. Remover aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case '1':
                cadastrar_aluno()
            case '2':
                ver_aluno()
            case '3':
                listar_alunos()
            case '4':
                remover_aluno()
            case '5':
                print("Encerrando sistema de notas.")
                break
            case _:
                print("Opção inválida.\n")

# Iniciar programa
menu()
