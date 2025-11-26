from math import factorial
num = int(input("digite um numero: "))
cont = 0
for num in range(num, 1):
    cont += 1
print(f"o fatorial de {num}! é  {cont + factorial(num)}")