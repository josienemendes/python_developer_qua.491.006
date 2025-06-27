
# dicionário

usuario = {
    "nome": "JOSIENE",
    "idade": 28,
    "email": "JOSIENE@GAMIL.COM"
    
}

# exibe as chaves
for chave in usuario:
    print(f"{chave.capitalize()}")
print('-' * 28)

# usuário informa a chave que deseja alterar
chave = input("Informe a chave que deseja alterar: ").lower().strip()

# verifica se a chave existe no dicionário
if chave in usuario:
    # usuário informa o novo valor
    novo_valor = input(f"Informe o novo valor para '{chave}': ").strip()
    
    # tenta converter para inteiro se a chave for "idade"
    if chave == "idade":
        try:
            novo_valor = int(novo_valor)
        except ValueError:
            print("Idade deve ser um número inteiro. Valor não alterado.")
        else:
            usuario[chave] = novo_valor
    else:
        usuario[chave] = novo_valor
    
    print("\nDados atualizados:")
    for k, v in usuario.items():
        print(f"{k.capitalize()}: {v}")
else:
    print("Chave não encontrada no dicionário.")
