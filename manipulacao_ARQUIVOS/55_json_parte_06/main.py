#importações
import json


try:
     #input 
     arquivo = input("Informe o nome do arquivo (sem extensao):").strip()

     #le o json e desserializa em um dicionario
     with open(F"{arquivo}.json", "r" , encoding="utf-8") as f:
        dados = json.load(f)
     
     #output
     print(F"{'-'*20} DADOS {'-'*20}\n")
     for dado in dados:
        for chave in dados:
           print(f"{chave.capitalize()}: {dados.get(chave)}")
        print("-"*40)
except Exception as e:
	
 print(f"nao foi possivel ler arquivo JSON. {e}.")
