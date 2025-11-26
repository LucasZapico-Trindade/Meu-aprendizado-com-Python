dados = list()
pessoas = list()
maior = menor = 0
while True:
    dados.append(str(input("digite um nome:")))
    dados.append(float(input("digite o peso da pessoa:")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    pergunta = str(input("quer continuar? [S/N] "))
    if pergunta in 'Nn':
        break

print(f"um total de {len(pessoas)} pessoas cadastradas")
print(f"o maior peso foi de {maior} quilos, peso de: ", end="")
for p in pessoas:
    if p[1] == maior:
        print(f"{p[0]} ", end= "")
print()
print(f"o menor peso foi de {menor} quilos, peso de ", end="")
for p in pessoas:
    if p[1] == menor:
        print(f"{p[0]} ", end= "")
print()




