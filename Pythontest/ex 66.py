cont=soma=0
while True:
    numero = int(input("digite o numero desejado:"))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f"a quantidade de numeros digitados foi {cont}, e a soma entre eles e de {soma}")
