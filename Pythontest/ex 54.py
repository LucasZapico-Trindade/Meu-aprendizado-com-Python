from datetime import date
hoje = date.today().year
idadeM = 0
idadem = 0
for pess in range(1, 8):
    ano = int(input("Digite o ano de nascimento: "))
    idade = hoje - ano
    if idade >= 18:
        idadeM += 1
    else:
        idadem += 1
print("{} pessoas sao maiores de idade".format(idadeM))
print("{} pessoas sao menores de idade".format(idadem))













