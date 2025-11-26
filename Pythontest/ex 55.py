maior = 0 # considerar ambos valores como  0
menor = 0
for p in range(1,6):
    peso = float(input("peso da {} pessoa:".format(p)))
    if peso == 1: # se o peso for igual a 1
        maior = peso # considerar ambas variaveis
        menor = peso
    else:
        if peso > maior: # condicional do maior peso
            maior = peso
        if peso < menor: # condicional do menor peso
            menor = peso
print(" o maior peso é {}".format(maior))
print(" o menor peso é {}".format(menor))
# dessa forma o programa vai entender que ele ta lendo o peso da primeira pessoa
# e considerando os dois valores como maior e menor, e so aplicar condicionais que
# verificam qual e o maior e qual e o menor

