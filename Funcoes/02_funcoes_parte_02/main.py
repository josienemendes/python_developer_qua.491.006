# funcao
def mostrar_mensagem(nome):
    return f'seja bem vindo!, {nome}!'

#programa principal
nome = input("Digite seu nome: ").strip().title()
print(mostrar_mensagem(nome))

