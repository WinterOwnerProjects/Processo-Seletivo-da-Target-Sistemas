import json
with open("dados.json") as file:
    data = json.load(file)
a = len(data)
valor_padrao = data[0]["valor"]
estado_padrao = data[0]["estado"]
soma = 0
for i in range(a):
    valor_padrao = data[i]["valor"]
    soma = soma + valor_padrao
for j in range(a):
    valor_padrao = data[j]["valor"]
    estado_padrao = data[j]["estado"]
    calculo_per = valor_padrao*100
    porcentagem = calculo_per / soma
    print(f"{estado_padrao} == {porcentagem:.2f}")

