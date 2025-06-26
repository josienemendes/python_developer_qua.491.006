import os
os.system("cls")


#declaração de variáveis

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

#ternario
result = "é maior de idade." if idade >= 18 else "é menor de idade."

#sáida
print(f"{nome} {result}")





