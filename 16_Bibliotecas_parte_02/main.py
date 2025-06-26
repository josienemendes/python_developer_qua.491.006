
# Importando bibliotecas
import os
import time

try:
    n = int(input("Informe um número inteiro: "))

    while n >= 0:
        os.system("cls")  # ou "clear" no Linux/macOS
        print(f"{n}...")
        time.sleep(1)
        n -= 1

except Exception as e:
    print(f"Não foi possível converter o valor informado para inteiro: {e}")

finally:
    print("Fim do programa")
