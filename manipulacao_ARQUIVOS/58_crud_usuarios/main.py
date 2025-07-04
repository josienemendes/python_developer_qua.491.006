#TODO Atividade_ JSON

""" Faça um CRUD (Create,Read,Update,Delete) em um JSON.
opções do menu:
- Criar novo arquivo Json (usuario ira informar o diretorio).
- Abrir arquivo Json( usuario ira informar o diretorio)
- Cadastrar novo usuario em um Json
- Listar todos os usuarios de um arquivo
- Pesquisar usuario atraves do valor de uma chave em um arquivo Json
- Alterar dados de um usuario em um arquivo Json
- Deletar usuario de um arquivo 
- Sair do programa

Dados do usuario:
- Nome
- data de nascimento
- cpf
- e-mail
- telefone
- filme favorito do usuario
"""


import json
import os

def criar_arquivo_json(caminho):
    if os.path.exists(caminho):
        print("Arquivo já existe.")
        return
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump([], f)
    print("Arquivo criado com sucesso.")

def abrir_arquivo_json(caminho):
    if not os.path.exists(caminho):
        print("Arquivo não encontrado.")
        return None
    with open(caminho, 'r', encoding='utf-8') as f:
        try:
            dados = json.load(f)
            if not isinstance(dados, list):
                print("Formato inválido. Esperado uma lista de usuários.")
                return None
            return dados
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
            return None

def salvar_arquivo_json(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def cadastrar_usuario(dados):
    usuario = {
        "nome": input("Nome: "),
        "data_nascimento": input("Data de nascimento: "),
        "cpf": input("CPF: "),
        "email": input("E-mail: "),
        "telefone": input("Telefone: "),
        "filme_favorito": input("Filme favorito: ")
    }
    dados.append(usuario)
    print("Usuário cadastrado com sucesso.")

def listar_usuarios(dados):
    if not dados:
        print("Nenhum usuário cadastrado.")
        return
    for i, usuario in enumerate(dados, 1):
        print(f"\nUsuário {i}:")
        for chave, valor in usuario.items():
            print(f"{chave}: {valor}")

def pesquisar_usuario(dados):
    chave = input("Pesquisar por qual campo? (nome, data_nascimento, cpf, email, telefone, filme_favorito): ")
    valor = input("Valor a pesquisar: ")
    encontrados = [u for u in dados if u.get(chave) == valor]
    if encontrados:
        for usuario in encontrados:
            print(usuario)
    else:
        print("Nenhum usuário encontrado.")

def alterar_usuario(dados):
    cpf = input("Informe o CPF do usuário a ser alterado: ")
    for usuario in dados:
        if usuario.get("cpf") == cpf:
            print("Usuário encontrado. Informe os novos dados (deixe em branco para manter o atual):")
            for chave in usuario:
                novo_valor = input(f"{chave} ({usuario[chave]}): ")
                if novo_valor:
                    usuario[chave] = novo_valor
            print("Usuário alterado com sucesso.")
            return
    print("Usuário não encontrado.")

def deletar_usuario(dados):
    cpf = input("Informe o CPF do usuário a ser deletado: ")
    for i, usuario in enumerate(dados):
        if usuario.get("cpf") == cpf:
            del dados[i]
            print("Usuário deletado com sucesso.")
            return
    print("Usuário não encontrado.")

def main():
    caminho = None
    dados = []
    while True:
        print("\nMenu:")
        print("1 - Criar novo arquivo Json")
        print("2 - Abrir arquivo Json")
        print("3 - Cadastrar novo usuário")
        print("4 - Listar todos os usuários")
        print("5 - Pesquisar usuário")
        print("6 - Alterar dados de um usuário")
        print("7 - Deletar usuário")
        print("8 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            caminho = input("Informe o caminho do novo arquivo JSON: ")
            criar_arquivo_json(caminho)
            dados = []
        elif opcao == "2":
            caminho = input("Informe o caminho do arquivo JSON: ")
            dados_lidos = abrir_arquivo_json(caminho)
            if dados_lidos is not None:
                dados = dados_lidos
        elif opcao == "3":
            if caminho:
                cadastrar_usuario(dados)
                salvar_arquivo_json(caminho, dados)
            else:
                print("Abra ou crie um arquivo primeiro.")
        elif opcao == "4":
            listar_usuarios(dados)
        elif opcao == "5":
            pesquisar_usuario(dados)
        elif opcao == "6":
            alterar_usuario(dados)
            if caminho:
                salvar_arquivo_json(caminho, dados)
        elif opcao == "7":
            deletar_usuario(dados)
            if caminho:
                salvar_arquivo_json(caminho, dados)
        elif opcao == "8":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()