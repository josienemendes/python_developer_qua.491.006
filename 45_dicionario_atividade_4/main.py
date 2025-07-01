"""
# Crie um programa que usa  dicionários com múltiplas informações por item,

Gerenciar estado (disponível/emprestado)

Usar match-case em um menu estruturado

"""


# Sistema de Biblioteca com Dicionário 

biblioteca = {}

# Cadastrar novo livro
def cadastrar_livro():
    codigo = input("Código do livro: ").strip()
    if codigo in biblioteca:
        print("Livro já cadastrado.\n")
        return

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano = input("Ano de publicação: ").strip()

    biblioteca[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "status": "Disponível",
        "emprestado_para": None
    }
    print(f"Livro '{titulo}' cadastrado com sucesso.\n")

# Emprestar livro
def emprestar_livro():
    codigo = input("Código do livro: ").strip()
    if codigo not in biblioteca:
        print("Livro não encontrado.\n")
        return

    if biblioteca[codigo]["status"] == "Emprestado":
        print("Livro já está emprestado.\n")
        return

    nome = input("Nome de quem vai pegar emprestado: ").strip()
    biblioteca[codigo]["status"] = "Emprestado"
    biblioteca[codigo]["emprestado_para"] = nome
    print(f"Livro emprestado para {nome} com sucesso.\n")

# Devolver livro
def devolver_livro():
    codigo = input("Código do livro: ").strip()
    if codigo not in biblioteca:
        print("Livro não encontrado.\n")
        return

    if biblioteca[codigo]["status"] == "Disponível":
        print("Este livro já está disponível.\n")
        return

    biblioteca[codigo]["status"] = "Disponível"
    biblioteca[codigo]["emprestado_para"] = None
    print("Livro devolvido com sucesso.\n")

# Ver detalhes de um livro
def ver_livro():
    codigo = input("Código do livro: ").strip()
    if codigo in biblioteca:
        l = biblioteca[codigo]
        print(f"\nTítulo: {l['titulo']}")
        print(f"Autor: {l['autor']}")
        print(f"Ano: {l['ano']}")
        print(f"Status: {l['status']}")
        if l['emprestado_para']:
            print(f"Emprestado para: {l['emprestado_para']}")
        print()
    else:
        print("Livro não encontrado.\n")

# Listar todos os livros
def listar_livros():
    if not biblioteca:
        print("Nenhum livro cadastrado.\n")
        return

    print("\n--- Catálogo da Biblioteca ---")
    for codigo, livro in biblioteca.items():
        status = livro['status']
        emprestado = f" (para {livro['emprestado_para']})" if livro['emprestado_para'] else ""
        print(f"[{codigo}] {livro['titulo']} - {livro['autor']} ({livro['ano']}) | {status}{emprestado}")
    print()

# Remover livro do acervo
def remover_livro():
    codigo = input("Código do livro: ").strip()
    if codigo in biblioteca:
        confirmar = input(f"Remover '{biblioteca[codigo]['titulo']}'? (s/n): ").strip().lower()
        if confirmar == 's':
            del biblioteca[codigo]
            print("Livro removido.\n")
        else:
            print("Remoção cancelada.\n")
    else:
        print("Livro não encontrado.\n")

# Menu principal
def menu():
    while True:
        print("=== MENU BIBLIOTECA ===")
        print("1. Cadastrar livro")
        print("2. Emprestar livro")
        print("3. Devolver livro")
        print("4. Ver detalhes de um livro")
        print("5. Listar todos os livros")
        print("6. Remover livro")
        print("7. Sair")

        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case '1':
                cadastrar_livro()
            case '2':
                emprestar_livro()
            case '3':
                devolver_livro()
            case '4':
                ver_livro()
            case '5':
                listar_livros()
            case '6':
                remover_livro()
            case '7':
                print("Encerrando sistema da biblioteca.")
                break
            case _:
                print("Opção inválida.\n")

# Iniciar o programa
menu()
