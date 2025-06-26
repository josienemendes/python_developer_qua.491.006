import os
os.system("cls")


meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

# Concatenar todos os meses separados por espaço
resultado = " ".join(meses)
print(resultado)

#exibe a lista
for i, mes in enumerate(meses):
    print(f"{i}: {mes}")