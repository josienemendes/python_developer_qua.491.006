import os
os.system("cls")

"""
# Atividade 05
 # TODO: Crie um programa que recebe do usuario o nome e a idade ,e em seguida , mostre um menu de filmes
 com suas respectivas classificações indicativas e salas de exibição. exemplo:
 *sala 1: a roda quadrada - livre
 *sala 2: a volta dos que mao foram - 12 anos
 *sala 3: poeira em alto mar - 14 anos
 *sala 4: as trancas do rei careca - 16 anos
 *sala 5: a vinganca do peixe frito - 18 anos

 * o usuario deve escolher a sala que esta passando o filme que deseja assistir.
  *Se o usuario estiver abaixo da idade minima ou mais pra ver o filme , o programa imprime o ingresso com nome do filme , a data e a hor da compra do ingresso
  e deje bom filme , e em seguida encerra o programa.
  *Se o usuario nao tiver idade minima para ver o filme , o programa bloqueia a sua entrada e re-exibe o menu de filmes
  para que ele possa escolher outro filme.
"""

from datetime import datetime

filmes = {
    1: {"titulo": "A Roda Quadrada", "classificacao": 0},
    2: {"titulo": "A Volta dos que Não Foram", "classificacao": 12},
    3: {"titulo": "Poeira em Alto Mar", "classificacao": 14},
    4: {"titulo": "As Trancas do Rei Careca", "classificacao": 16},
    5: {"titulo": "A Vingança do Peixe Frito", "classificacao": 18},
}

def mostrar_menu():
    print("\nMenu de filmes disponíveis:")
    for sala, info in filmes.items():
        faixa = "livre" if info["classificacao"] == 0 else f"{info['classificacao']} anos"
        print(f"* Sala {sala}: {info['titulo']} - {faixa}")

def comprar_ingresso(nome, filme):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print("\n*** INGRESSO ***")
    print(f"Nome: {nome}")
    print(f"Filme: {filme['titulo']}")
    print(f"Data e hora da compra: {agora}")
    print("BOM FILME!")
    print("****************\n")

def programa():
    nome = input("Digite seu nome: ").strip()
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("Idade inválida. Tente novamente.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido para a idade.")

    while True:
        mostrar_menu()
        try:
            escolha = int(input("Escolha a sala do filme que deseja assistir (1-5): "))
        except ValueError:
            print("Por favor, digite um número válido para a sala.")
            continue

        match escolha:
            case 1 | 2 | 3 | 4 | 5:
                filme_escolhido = filmes[escolha]
                if idade >= filme_escolhido["classificacao"]:
                    comprar_ingresso(nome, filme_escolhido)
                    break
                else:
                    print(f"Desculpe, você não tem a idade mínima para assistir a esse filme ({filme_escolhido['classificacao']} anos).")
                    print("Por favor, escolha outro filme.\n")
            case _:
                print("Sala inválida, tente novamente.")

if __name__ == "__main__":
    programa()
