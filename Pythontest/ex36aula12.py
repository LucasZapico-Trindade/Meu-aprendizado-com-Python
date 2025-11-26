valor = float(input("qual é o valor da casa que voce deseja comprar? R$"))
sal = float(input("qual e a sua renda mensal? R$"))
tempo = int(input("em quantos anos voce deseja pagar a casa?"))
prestacao  = valor / (tempo * 12)
if prestacao <= sal * 0.30:
    print(" seu emprestimo foi aprovado e esta no valor de R${} por parcela!!".format(prestacao))
else:
    print(" seu emprestimo foi reprovado, pois o valor da parcela de {} excede 30% do seu salario!!".format(prestacao))











