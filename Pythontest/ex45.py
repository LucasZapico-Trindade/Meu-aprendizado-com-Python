from random import randint
from time import sleep

itens = ("pedra", "papel", "tesoura")
computador = randint(0, 2)
print("""Escolha sua opcao!!
[0] pedra
[1] papel
[2] tesoura""")
jogador = int(input("qual a sua opcao? "))
print("JO"), sleep(1)
print("KEN"), sleep(1)
print("PO!!!"),sleep(1)
print("-=" * 15)
print("computador jogou {}".format(itens[computador]))
print("jogador jogou {}".format(itens[jogador]))
print("-=" * 15)
if computador == 0:
    if jogador == 0:
        print("empate")
    elif jogador == 1:
        print("jogador vence")
    elif jogador == 2:
        print("computador vence")
elif computador == 1:
    if jogador == 0:
        print("computador vence")
    elif jogador ==1:
        print("empate")
    elif jogador == 2:
        print("jogador vence")
elif computador == 2:
    if jogador == 0:
        print("jogador vence")
    elif jogador == 1:
        print("computador vence")
    elif jogador == 2:
        print("empate")

