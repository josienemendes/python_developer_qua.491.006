import json
import os

try:
    arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
    caminho_arquivo = f"{arquivo}.json"

    # Carrega o arquivo se existir, senão cria lista vazia
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            pessoas = json.load(f)
    else:
        pessoas = []

    pessoa = {}

    # Coleta e trata os dados
    pessoa["nome"] = input("Nome: ").strip().title()
    pessoa["idade"] = int(input("Idade: ").strip())
    pessoa["cpf"] = input("CPF: ").strip()
    pessoa["rg"] = input("RG: ").strip()
    pessoa["data_nasc"] = input("Data de nascimento (dd/mm/aaaa): ").strip()
    pessoa["sexo"] = input("Sexo: ").strip().lower()
    pessoa["signo"] = input("Signo: ").strip().capitalize()
    pessoa["mae"] = input("Nome da mãe: ").strip().title()
    pessoa["pai"] = input("Nome do pai: ").strip().title()
    pessoa["email"] = input("Email: ").strip().lower()
    pessoa["senha"] = input("Senha: ").strip()
    pessoa["cep"] = input("CEP: ").strip()
    pessoa["endereco"] = input("Endereço: ").strip().title()
    pessoa["numero"] = int(input("Número: ").strip())
    pessoa["bairro"] = input("Bairro: ").strip().title()
    pessoa["cidade"] = input("Cidade: ").strip().title()
    pessoa["estado"] = input("Estado: ").strip().upper()
    pessoa["telefone_fixo"] = input("Telefone fixo: ").strip()
    pessoa["celular"] = input("Celular: ").strip()

    altura_raw = input("Altura (ex: 1,75): ").strip().replace(",", ".")
    pessoa["altura"] = float(altura_raw)

    pessoa["peso"] = int(input("Peso: ").replace(",",","))
    pessoa["tipo_sanguineo"] = input("Tipo sanguíneo: ").strip()
    pessoa["cor"] = input("Cor favorita: ").strip()

    # Adiciona a nova pessoa à lista
    pessoas.append(pessoa)

    # Salva no arquivo
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(pessoas, f, ensure_ascii=False, indent=4)
    with open(F"{arquivo}.json", "r" , encoding="utf-8") as f:
        pessoas = json.load(f)
        
    print(F"{'-'*20} LISTA DE PESSOAS {'-'*20}")
    for pessoa in pessoas:
        for chave in pessoa:
            print(F"{chave.capitalize()}: {pessoa.get(chave)}")
        print('-'*40)

    print(f"Pessoa cadastrada com sucesso!")

except Exception as e:
    print(f"Não foi possivel inserir uma pessoa: {e}")
