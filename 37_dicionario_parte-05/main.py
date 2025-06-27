# dicionario 
usuario = {
"nome": "JOSIENE",
"idade": 28,
"email": "JOSIENE@GMAIL.COM"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

    #adicionando nova chave

usuario["profissao"] = input ("informe a profissao: ").strip ()

print("-"*28)
for chave in usuario:
    valor = usuario.get(chave)
    if isinstance(valor, str):
        valor = valor.title()
    print(f"{chave.capitalize()}: {valor}")


