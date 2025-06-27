#DICIONARIO
usuario = {
    "nome": "JOSIENE",
    "idade": 28,
    "email": "JOSIENE@GAMIL.COM",
    "profissao": "programador"
}

#exibe os valores
for chave in usuario:

    print(f"{chave.capitalize()}: {usuario.get(chave)}")
    
