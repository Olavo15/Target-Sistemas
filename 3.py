import json

def carregar_faturamento(arquivo):
    with open(arquivo, 'r') as file:
        dados = json.load(file)
    return dados

def calcular_faturamento(faturamento_diario):
    
    faturamento_valido = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]
    
    
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    
    
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    
    
    dias_acima_da_media = len([valor for valor in faturamento_valido if valor > media_mensal])
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media


arquivo_json = 'dados.json'
faturamento_diario = carregar_faturamento(arquivo_json)
menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)

print(f"Menor valor de faturamento ocorrido em um dia do mês: R$ {menor:.2f}")
print(f"Maior valor de faturamento ocorrido em um dia do mês: R$ {maior:.2f}")
print(f"Número de dias no mês com faturamento superior à média mensal: {dias_acima_media} dias")
