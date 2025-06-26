import os
os.system("cls")

""" 
# TODO:
# Atividade 03 - Crie um programa que faça as seguintes operações:
- calcular area de um circulo
- calcular tamanho de uma circunferencia
- sair do programa
# NOTE - para cada loop,o programa devera limpar o terminal 

"""
import os
import time
import math

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_area(raio):
    return math.pi * raio ** 2

def calcular_circunferencia(raio):
    return 2 * math.pi * raio

while True:
    limpar_tela()
    print("=== MENU ===")
    print("1 - Calcular área de um círculo")
    print("2 - Calcular comprimento de uma circunferência")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        try:
            raio = float(input("Informe o raio do círculo: "))
            area = calcular_area(raio)
            print(f"A área do círculo é: {area:.2f}")
        except ValueError:
            print("Valor inválido! Digite um número.")
    
    elif opcao == '2':
        try:
            raio = float(input("Informe o raio da circunferência: "))
            circunferencia = calcular_circunferencia(raio)
            print(f"O comprimento da circunferência é: {circunferencia:.2f}")
        except ValueError:
            print("Valor inválido! Digite um número.")
    
    elif opcao == '3':
        print("Saindo do programa...")
        time.sleep(1)
        break
    
    else:
        print("Opção inválida! Tente novamente.")
    
    input("\nPressione Enter para continuar...")
    time.sleep(1)
    limpar_tela()

    # FIM DO PROGRAMA!     


