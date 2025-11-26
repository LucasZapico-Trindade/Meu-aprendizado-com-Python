somaidade = 0 #variavel para somar as 4 idades.
mediaidade = 0 # variavel para calcular a media.
maioridadehomem = 0 # variavel para calcular a idade do homem mais velho
nomevelho = " " #variavel para mostrar a o nome do mais velho
totmulher20 = 0 # variavel para mostrar o total de mulheres com menos de 20 anos
for d in range(1, 5):
    print("--------{} pessoa---------- ".format(d))
    nome = str(input("nome:"))
    idade = int(input("Idade:"))
    sexo = str(input("sexo[M/F]:")).strip()
    somaidade += idade # somar as 4 idades
    if d == 1 and sexo in "Mm": # se d for igual a 1 e sexo for masculino
        maioridadehomem = idade  #  a maior idade vai ser igual a idade
        nomevelho = nome # e o nome do velho vai ser igual ao nome
    if sexo in "Mm" and idade > maioridadehomem: #se caso sexo for Masculino e a idade for maior que a maior idade do homem
        maioridadehomem = idade #a maior idade vai ser igual a idade
        nomevelho = nome # e o nome do velho vai ser igual a nome
    if sexo in "Ff" and idade < 20: # e se caso o sexo for feminino e a idade for  menor que 20
        totmulher20 += 1 #o total de mulheres vai ser o total + 1


mediaidade = somaidade / 4
print("a media de idade do grupo é de {} anos".format(mediaidade))
print(" o homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))
print("a quantidade de mulheres com menos de 20 anos: {}".format(totmulher20))
# passo um, calcular a media de idade dos integrantes!!




