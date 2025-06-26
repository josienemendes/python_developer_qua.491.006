import os
os.system("cls")



#declaracão de variaveis
aluno = input("informe o nome do aluno:")
media = float(input("informe a média do aluno:").replace(",", "."))

#estrutura de decisão
if media >= 0 or media <= 10:
    if media >= 7:
        print(f"{aluno} está aprovado.")
    elif media >= 5:
        print(f"{aluno} está de recuperação.")
    else:
        print(f"{aluno} está reprovado.")

else:
    print("nota inválida.")

