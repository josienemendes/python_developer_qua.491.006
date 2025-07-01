

import random
from datetime import datetime

usuarios = []

def cadastrar_usuario():
    print("\n📥 Cadastro de novo usuário:")
    nome = input("Nome completo: ").strip()
    for usuario in usuarios:
        if usuario["cpf"] == input("Digite o CPF para verificação: ").strip():
            print("❌ CPF já cadastrado.")
            return
    
    data_nasc = input("Data de nascimento (dd/mm/aaaa): ").strip()
    email = input("Email: ").strip()
    cpf = input("CPF: ").strip()
    telefone = input("Telefone: ").strip()
    genero = input("Gênero (M/F/Outro): ").strip()
    
    agora = datetime.now()
    data_cadastro = agora.strftime("%d/%m/%Y")
    hora_cadastro = agora.strftime("%H:%M:%S")

    usuarios.append({
        "nome": nome,
        "data_nasc": data_nasc,
        "email": email,
        "cpf": cpf,
        "telefone": telefone,
        "genero": genero,
        "data_cadastro": data_cadastro,
        "hora_cadastro": hora_cadastro
    })

    print(f"\n✅ Usuário '{nome}' cadastrado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("ℹ️ Nenhum usuário cadastrado.")
        return
    print("\n📋 Lista de usuários cadastrados:")
    for idx, usuario in enumerate(usuarios, start=1):
        print(f"\n--- Usuário {idx} ---")
        for chave, valor in usuario.items():
            print(f"{chave.capitalize().replace('_', ' ')}: {valor}")

def alterar_usuario():
    cpf = input("Digite o CPF do usuário a ser alterado: ").strip()
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("🔄 Alterando dados do usuário:")
            usuario["nome"] = input("Novo nome completo: ").strip()
            usuario["data_nasc"] = input("Nova data de nascimento (dd/mm/aaaa): ").strip()
            usuario["email"] = input("Novo email: ").strip()
            usuario["telefone"] = input("Novo telefone: ").strip()
            usuario["genero"] = input("Novo gênero (M/F/Outro): ").strip()
            print("✅ Dados alterados com sucesso!")
            return
    print("❌ Usuário não encontrado.")

def excluir_usuario():
    cpf = input("Digite o CPF do usuário a ser excluído: ").strip()
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuarios.remove(usuario)
            print(f"✅ Usuário com CPF {cpf} removido com sucesso!")
            return
    print("❌ Usuário não encontrado.")

def sortear_usuario():
    if not usuarios:
        print("⚠️ Nenhum usuário cadastrado para sortear.")
        return
    sorteado = random.choice(usuarios)
    print(f"\n🎯 Usuário sorteado:")
    for chave, valor in sorteado.items():
        print(f"{chave.capitalize().replace('_', ' ')}: {valor}")

def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Cadastrar novo usuário")
        print("2. Listar todos os usuários")
        print("3. Alterar dados de um usuário")
        print("4. Excluir um usuário")
        print("5. Sortear um usuário")
        print("6. Sair")
        opcao = input("Escolha uma opção (1-6): ")

        match opcao:
            case "1":
                cadastrar_usuario()
            case "2":
                listar_usuarios()
            case "3":
                alterar_usuario()
            case "4":
                excluir_usuario()
            case "5":
                sortear_usuario()
            case "6":
                print("👋 Encerrando o programa. Até mais!")
                break
            case _:
                print("❌ Opção inválida. Tente novamente.")

# Inicia o programa
menu()
