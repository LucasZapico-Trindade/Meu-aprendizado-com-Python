numero = (int(input("digite um numero:")), int(input("digite um numero:")), int(input("digite um numero:")),
          int(input("digite um numero:")))
print(f"os numeros digitados foram {numero}")
print(f"o valor 9 apareceu {numero.count(9)} vezes")
if 3 in numero:
    print(f"o numero 3 apareceu na {numero.index(3) + 1} posicao")
else:
    print("o valor 3 nao foi digitado em nenhuma posicao")
print(f"os valores pares digitados foram")
for n in numero:
    if n % 2 == 0:
        print(n, end=" ")



