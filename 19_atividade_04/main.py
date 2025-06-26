import os
os.system("cls")
""""
#atividade 04
#TODO: Crie um programa que mostra a hora atual sempre sendo atualizado  cada
segundo.
#NOTE - para interromper o programa,use a tecla Ctrl + C
"""

import os
import time
from datetime import datetime

def limpar_tela():
    # Limpa a tela do terminal dependendo do sistema operacional
    os.system("cls" if os.name == "nt" else "clear")

try:
    while True:
        limpar_tela()
        agora = datetime.now().strftime("%H:%M:%S")
        print("Hora atual:", agora)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
    os.system("cls" if os.name == "nt" else "clear")
    print("Saindo do programa...")
    