#importacoes
import modulo as m



# programa principal
if __name__ == "__main__":   # ALGORITMO principal
    while True:
        print("1 -calcular quadrado")
        print("2 -calcular retangulo")
        print("3 -calcular triangulo")
        print("4 -sair")

        opcao = input("Digite a opcao desejada: ").strip()
        m.limpar_tela()
        match opcao:
            case "1":
                try:
                   l=int(input("Digite o lado do quadrado: "))
                   a= m.area_quadrado(l)
                   print(f"A area do quadrado e: {a}")
                except Exception as e:
                    print(f"erro: {e}")
                finally:
                    continue

            case "2":
                    try: 
                        b = int(input("Digite a base do retangulo: "))
                        h = int(input("Digite a altura do retangulo: "))
                        a = m.area_retangulo(b, h)

                        print(f"A area do retangulo e: {a}") 
                    except Exception as e:
                        print(f"erro. {e}")
                    finally:
                        continue
            case "3":
                    try: 
                       b = int(input("Digite a base do triangulo: "))
                       h = int(input("Digite a altura do triangulo: "))
                       a = m.area_triangulo(b, h)

                       print(f"A area do triangulo e: {a}")

                    except Exception as e :
                        print(f"erro: {e}")
                    finally:
                        continue
            case "4":
                    try:
                        r =(input("Digite o raio do circulo: "))
                        a = m.area_circulo(r)
                        print(f"A area do circulo e: {a}")
                    except Exception as e:
                        print(f"erro: {e}")
                    finally:
                        continue