from datetime import date
ano = date.today().year
sexo = input("voce é homem ou mulher?").strip()
if sexo == "homem":
    nasc = int(input("qual e o seu ano de nascimento?"))
    idade = ano - nasc
    if idade < 18:
        temp = 18 - idade
        print("sua idade e de {} anos ainda falta {} anos para voce se alistar".format(idade, temp))
    elif idade > 18:
        temp = idade - 18
        print("voce tem {} anos, seu ano de alistamento foi ha {} anos atras  ".format(idade, temp))
    else:
        print("voce tem {} anos, deve se alistar imdiatamente".format(idade))
else:
    print("mulheres nao sao elegiveis para alistamento")




