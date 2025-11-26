lista = []
pares = []
impares = []
while True:
    n = (int(input("digite um numero: ")))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    r = str(input("quer continuar? [S/N] ")).upper().strip()[0]
    if r in 'Nn':
        break
print(f"a sua lista completa: {lista}")
print(f"a sua lista de numeros pares: {pares}")
print(f"a sua lista de numeros impares: {impares}")