numeros = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o valor {c}: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print(f'Valores pares: {sorted(numeros[0])}')
print(f'Valores impares: {sorted(numeros[1])}')
