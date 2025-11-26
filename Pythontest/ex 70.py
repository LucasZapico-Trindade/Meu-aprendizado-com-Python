total = totmil = menor = cont = 0
barato = " "
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input("preco do produto:"))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print(f"o total da sua compra foi de {total}")
print(f"voce tem {totmil} produtos acima de mil reais")
print (f"o produto mais barato custa {menor} e o nome dele é {barato}")






















