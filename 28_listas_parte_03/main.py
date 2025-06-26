import os
os.system("cls")
import os

# lista
nomes = ["Fulano", "Cicrano", "Beltrano", "Joao", "Maria", "Raniele"]

# Exibe a lista
for i in range(len(nomes)):
    print(f"{i}: {nomes[i]}")
print("-" * 60)

try:
    i = int(input("Informe o índice que deseja separar: "))
    if 0 <= i < len(nomes):
        nome_isolado = nomes.pop(i)


 

        # Limpa a tela dependendo do sistema operacional
        os.system("cls" if os.name == "nt" else "clear")

        print(f"{nome_isolado}: separado com sucesso!")

        #lista exibe os valores sem o item isolado
        for i in range(len(nomes)):
            print(f"{i}: {nomes[i]}")
    else:
        print("Índice fora do intervalo da lista.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
