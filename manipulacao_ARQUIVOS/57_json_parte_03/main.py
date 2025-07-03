import json

try:
    # Entrada do nome do arquivo (sem .json)
    arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()

    # 1. Lê o arquivo JSON e desserializa para lista de dicionários
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        lista = json.load(f)

    # 2. Aplica conversões nos dados (strings para MAIÚSCULAS)
    for item in lista:
        for chave in item:
            if isinstance(item[chave], str):
                item[chave] = item[chave].upper()

    # 3. Serializa novamente os dados modificados para o mesmo arquivo
    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

    # 4. Mensagem de confirmação
    print(f"\n✅ Dados convertidos e salvos com sucesso em '{arquivo}.json'.")
    print(f"\n{'-'*20} DADOS TRATADOS {'-'*20}\n")
    for item in lista:
        for dado, valor in item.items():
            print(f"{dado.capitalize()}: {valor}")
        print("-" * 40)

except Exception as e:
    print(f"\n❌ Não foi possível ler ou processar o arquivo JSON. Erro: {e}")
