valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print("valor duplicado, nao irei adicionar!")
    r = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    if r in 'Nn':
        break
print(f"voce digitou os numeros {sorted(valores)}")

