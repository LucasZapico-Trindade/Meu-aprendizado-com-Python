print ("{:=^40}".format("LOJAS LUCAS TRINDADE"))
valor = float(input("quanto deu sua compra? R$"))
print("analisando valores, aguarde..." )
print("""Escolha sua forma de pagamento:
[1] A vista, dinheiro ou cheque!
[2] a vista no cartao!
[3] em ate 2x no cartao!
[4] 3x ou mais no cartao!""")
pag = float(input("qual a forma de pagamento?"))
if pag == 1:
    print("Voce escolheu a forma de pagamento com desconto de 10%!!")
    valord = valor - (valor * 0.10)
    print("a sua compra ficou no valor de R${:.2f}".format(valord))
elif pag == 2:
    print("voce escolheu a forma de pagamento com desconto de 5%!!")
    valord = valor - (valor * 0.05)
    print("a sua compra ficou no valor de R${:.2f}".format(valord))
elif pag == 3:
    print("voce escolheu a forma de pagamento sem desconto!!")
    valord = valor / 2
    print(" a sua compra parcelada fica 2x de R${:.2f}".format(valord))
elif pag == 4:
    print("voce escolheu a forma de pagamento com juros!!")
    valorj = valor + (valor * 0.20)
    parc = int(input("quantas parcelas?"))
    valorp = valorj / parc
    print("a sua compra ficou parcelada em {}X de R${:.2f}".format(parc, valorj))
    print("a sua compra no final vai ficar no valor de R${:.2f}".format(valorj))
else:
    pag = 0
    print("opcao de pagamento invalida, tente novamente!!")
    











