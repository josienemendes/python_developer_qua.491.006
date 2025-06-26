import os
os.system("cls")

# TODO -ATIVIDADE 01

#laço de repetição
while True:
    #tratamento de execessao

 try:
        #entrada de dados
        etanol= float(input("Informe o valor do etanol em reais:R$ ").replace(",", "."))
        gasolina = float(input("Informe o valor da gasolina em reais:R$ ").replace(",", "."))
        calculo = (etanol / gasolina) * 100
        result = "gasolina" if (calculo) >= 0.7 else "etanol"

        print(f"Resultado = {calculo:.2f}%. compensa abastecer com {result}.")

        opcao = input("Deseja refazer o calculo? (s/n): ").lower().strip()
        match opcao:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção inválida!")
                continue

 except Exception as e:
        
        print(f"Não foi possivel executar operação.")
        continue
 
 print("Programa encerrado.")



           
    




        
   




