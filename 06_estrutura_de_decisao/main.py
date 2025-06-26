import os
os.system

# declarção de variaveis
nome = input("informe seu nome: ")
idade = int(input("informe sua idade: "))

#estrutura de decisão
if idade >= 18:
    print(f"{nome} é maior de idade.")
else:
    print(f"{nome} é menor de idade.")


