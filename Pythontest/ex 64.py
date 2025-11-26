soma = contador = num = 0
numero = int(input("numero?:"))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input("numero?:"))
print(f"a quantidade de numeros digitados foi {contador}")
print(f"a soma entre seus numeros é de {soma}")
