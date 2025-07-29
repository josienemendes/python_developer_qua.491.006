  #importacoes
import os



# funcoes
def area_quadrado(lado):
    a = lado**2
    return a

def area_retangulo(base, altura):
    a = base * altura
    return a

def area_triangulo(base, altura):
    a = (base * altura) / 2
    return a

def limpar_tela():
    import os
    os.system("cls" if os.name == "nt" else "clear")
