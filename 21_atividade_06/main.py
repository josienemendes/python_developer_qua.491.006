import os
os.system("cls")

"""
# Atividade 06
# TODO: Crie um programa em que o usuario informa um ano e o programa exibe todo o 
calendario  do ano informado pelo usuario.
# NOTE- o usuario podera informar qualquer ano a partir de 1900.
# NOTE- Use a biblioteca "calendar"
"""
import calendar

def exibir_calendario():
    while True:
        try:
            ano = int(input("Informe o ano (a partir de 1900): "))
            if ano < 1900:
                print("Por favor, informe um ano igual ou maior que 1900.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro para o ano.")

    print(f"\nCalendário do ano {ano}:\n")
    print(calendar.calendar(ano))

if __name__ == "__main__":
    exibir_calendario()
    input("\nPressione Enter para sair...")
    os.system("cls" if os.name == "nt" else "clear")

    def encerrar_programa():
       print("PROGRAMA ENCERRADO!")