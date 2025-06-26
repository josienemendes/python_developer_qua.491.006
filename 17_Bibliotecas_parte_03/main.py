import os
os.system("cls")


#Importando bibliotecas
import math as m


print(f"O número pi é: {m.pi}") # exibe o número pi
print(F" numero do pi: {m.pi}") # exibe o número pi com duas casas decimais

# Raiz quadrada 
try:
    n = int(input("Informe um número inteiro: "))
    print(f"A raiz quadrada de {n} é: {m.sqrt(n):.2f}")  # exibe a raiz quadrada do número informado
except Exception as e:
    print(f"Não foi possível calcular a raiz quadrada. {e}")

    

