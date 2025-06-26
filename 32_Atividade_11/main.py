import os
os.system("cls")

""" #TODO - Atividade :crie um programa que receba de um professor 
varias notas de um aluno de 0 a 10 (não importa quantas notas ), Ao 
final do programa , a media das notas devera ser calculada e 
informada , e em seguida no programa ira informar se o aluno:
- Foi aprovado,caso media for maior ou igual a 7
- Ficou de recuperacao, caso media for entre 5 e7
- Foi reprovado,caso media for menor que 5."""

#Exibe listas
notas = []

print("Digite as notas do aluno (de 0 a 10).")
print("Digite 'sair' para encerrar e calcular a média.\n")

while True:
    entrada = input("Informe uma nota: ")
    
    if entrada.lower() == "sair":
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite um número entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite um número ou 'sair'.")

# Verifica se há notas para calcular
if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia do aluno: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado ✅")
    elif 5 <= media < 7:
        print("Situação: Recuperação ⚠️")
    else:
        print("Situação: Reprovado ❌")
else:
    print("Nenhuma nota foi inserida.")

    #fim do programa
