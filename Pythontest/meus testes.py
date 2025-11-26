galera = list()
dado = list()
totmaio = totmeno = 0
for c in range(0, 4):
    dado.append(str(input('Digite um nome: ')))
    dado.append(int(input('Digite um numero: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} e maior de idade")
        totmaio += 1
    else:
        print(f"{p[0]} e menor de idade")
        totmeno += 1

print(f"temos {totmaio} maiores e {totmeno} menor")







