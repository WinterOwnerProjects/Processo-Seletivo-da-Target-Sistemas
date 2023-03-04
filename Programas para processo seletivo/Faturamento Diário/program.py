import json

with open("dados.json") as file:
    data = json.load(file)
menor_valor = data[0]["valor"]
maior_valor = data[0]["valor"]
a = len(data)
for i in range(a):
    data_valor = data[i]["valor"]
    data_dias = data[i]["dia"]
    if data_valor != 0.0:
        if data_valor < menor_valor:
            menor_valor = data_valor
            menor_dia = data_dias
        if data_valor > maior_valor:
            maior_valor = data_valor
            maior_dia = data_dias
data_valor_m = data[0]["valor"]
count = 0
for o in range(a-1):
    data_valor_m = data[o]["valor"]
    data_soma = data_valor_m + data[o+1]["valor"]
    data_media = data_soma/a
    if data_valor_m > data_media:
        count += 1
print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[FATURAMENTO MENSAL]-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-
        O MAIOR valor de faturamento ocorrido foi no dia: {maior_dia} e teve o valor de: {maior_valor}
        E o MENOR valor de faturamento ocorrido foi no dia: {menor_dia} e teve o valor de: {menor_valor}

        O número de dias no mês em que o valor de faturamento diário foi superior à média mensal é: {count}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-
""")    



