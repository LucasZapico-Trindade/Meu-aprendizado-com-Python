lista = []
while True:
    n = int(input("digite um numero: "))
    lista.append(n)
    r = str(input("quer continuar? [S/N] ")).strip().upper()[0]
    if r in 'Nn':
        break
print(f"voce digitou {len(lista)} elementos")
lista.sort(reverse=True)
print(f"a sua lista em forma decrescente: {lista}")
if 5 in lista:
    print("o numero 5 esta na lista")
else:
    print("o numero 5 nao esta na lista")

