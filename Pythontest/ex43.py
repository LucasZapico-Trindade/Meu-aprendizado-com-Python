peso = float(input("qual e o seu peso?"))
altura = float(input("qual a sua altura?"))
imc = peso / (altura **2)
if imc < 18.5:
    print("seu IMC e de {:.1f}, voce esta abaixo do peso!!".format(imc))
elif imc <= 25:
    print("seu IMC e de {:.1f}, voce esta no peso ideal".format(imc))
elif imc <= 30:
    print("seu IMC e de {:.1f}, voce esta com sobrepeso".format(imc))
elif imc <= 40:
    print("seu IMC e de {:.1f}, voce esta com obesidade".format(imc))
else:
    print(" seu IMC e de {:.1f}, voce esta com obesidade morbida".format(imc))




