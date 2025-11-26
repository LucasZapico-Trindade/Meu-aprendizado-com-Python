r1 = float(input("digite seu segmento:"))
r2 = float(input("digite seu segundo segmento:"))
r3 = float(input("digite seu terceiro segmento:"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("os segmentos acima formam um triangulo!!")
    if r1 == r2 == r3:
        print("os segmentos formam um triangulo equilatero!!")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("os segmentos formam triangulo isosceles!!")
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print("os segmentos formam um triangulo escaleno!!")
else:
    print("os segmentos nao podem formar um triangulo!!")

