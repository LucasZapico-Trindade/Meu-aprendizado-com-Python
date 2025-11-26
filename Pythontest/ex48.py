lista = []
for num in range(1, 501, 2):
    if num % 3 == 0:
        lista.append(num)
soma = 0
for num in lista:
    soma = soma + num
print("a quantidade de numeros multiplos de 3 e {} e a soma deles e {}".format(len(lista), soma))














