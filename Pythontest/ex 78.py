valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
                menor = valores[c]
print(f"os valores digitados foram {valores}")
print(f"o maior valor digitado foi {maior}  e o menor foi {menor}")
print(f"o maior valor digitado esta na posicao {valores.index(maior)+1}")
print(f"o menor valor digitado esta na posicao {valores.index(menor)+1}")


