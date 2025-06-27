# dicionário
usuario = {
    "nome": "JOSIENE",
    "idade": 28,
    "email": "JOSIENE@GMAIL.COM"
}

# exibe o dicionário atual
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
print("-" * 28)

# usuário informa a chave que deseja excluir
chave_excluir = input("Informe a chave que deseja excluir: ").lower().strip()

# verifica se a chave existe e exclui
if chave_excluir in usuario:
    del usuario[chave_excluir]
    print(f"Chave '{chave_excluir}' excluída com sucesso!")
else:
    print(f"A chave '{chave_excluir}' não existe no dicionário.")

print("-" * 28)

# exibe o dicionário atualizado
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
