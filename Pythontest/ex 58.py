from random import randint
print("""Sou seu computador...
Acabei de pensar em um numero entre 0 e 10.
Sera que voce consegue adivinhar qual foi?""")
numero = randint(0, 11)
palpite = int(input("qual e o seu palpite?"))
cont = 0
while palpite != numero:
    print("voce errou, digite novamente")
    palpite = int(input("qual e o seu palpite?"))
    cont += 1
print("parabens, voce acertou e precisou de {} tentativas eu escolhi o numero {}".format(cont, numero))



