resp = "S"
media = cont = soma = maior = menor = 0
while resp in "Ss":
    numero = int(input("digite um numero:"))
    cont += 1
    soma += numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
                menor = numero
    resp = str(input("quer continuar?[S/N]")).upper().strip()[0]
media = soma / cont
print(f"voce digitou {cont} numeros \nA media entre seus numeros é {media:.1f}")
print(f"o seu maior numero é {maior} e o menor é {menor}")


