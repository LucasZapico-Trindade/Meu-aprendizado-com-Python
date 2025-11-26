from datetime import date
ano = date.today().year
nasc = int(input("qual e o ano de nascimento?"))
idade = ano - nasc
if idade <= 9:
    print("atleta MIRIM")
elif idade <= 14:
    print("atleta INFANTIL")
elif idade <= 19:
    print("atleta JUNIOR")
elif idade <= 25:
    print("atleta SENIOR")
else:
    print("atleta MASTER")
    






