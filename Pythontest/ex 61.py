primeiro = int(input("digite o termo: "))
razao = int(input("digite sua razao:"))
termo = primeiro
cont = 1
while cont <= 10:
    print(f"{termo} -> ", end="")
    termo += razao
    cont += 1
print("fim")
