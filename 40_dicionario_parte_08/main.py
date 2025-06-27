# dicionario

chaves = ("nome" , "idade", "E-mail" , "telefone", "profissao")
usuario = {
    chaves[0]: "josiene mendes",
    chaves[1]: "28",
    chaves[2]: "josiene@gmail.com",
    chaves[3]: "(61)99860-7397",
    chaves[4]: "programador"

}

for chave in chaves:
    print(f"{chave}:{usuario.get(chave)}")

    