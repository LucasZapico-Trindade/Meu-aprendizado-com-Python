from random import randint                    # importar o randint para o computador escolher um numero.
print("-=" * 12)
print("JOGO DO PAR OU IMPAR")
print("-=" * 12)
v = 0
# primeiro de tudo o layout do programa.




while True:                       # laco infinito, enquanto a iteracao for  verdadeira
    jogador = int(input("digite um numero: "))                         # perguntar ao usuario o numero
    computador = randint(0, 11)                         # escolha do computador
    total = jogador + computador                   # a soma entre o numero do usuario e o numero escolhido pelo computador
    tipo =" "                # uma variavel tipo vazia para a declaracao dela seja uma condicao
    # depois um laco infinito com as variaveis para o programa sempre fazer eles nas condicoes impostas



    while tipo not in "PI":                 #enquanto a variavel tipo nao ter as letras p ou i
        tipo = str(input("par ou impar:")).strip().upper()[0]               #pergunto ao usuario se ele quer par ou impar
    print(f"voce jogou {jogador} e o computador {computador} no total fica {total}")
    # variavel enquanto, especificando a variavel tipo entre par ou impar, logo depois perguntando ao usuario
    # qual ele escolher e depois printando as escolhas de cada um












    if tipo == "P":                 #se tipo for p
        if total % 2 == 0:                       #se o total dividido por 2 for igual a zero
            print(f"voce venceu")
            v += 1                    # contador de vitorias
        else:               #caso contrario
            print(f"voce perdeu")
            break                      #interromper o loop caso o jogador perder
    # variavel caso a escolha for par






    elif tipo == "I":                   # e se tipo for igual a Impar
        if total % 2 == 1:                             #se o total for dividido por 2 e o resultado der 1
            print(f"voce venceu")
            v += 1                                 # contador de vitorias
        else:                 # caso contrario
            print(f"voce perdeu")
            break #interrompe o laco caso perca
   #variavel caso a escolha for impar



    print("vamos jogar novamente...")                     #dentro do loop sempre que o usuario vencer
print(f"game over! voce venceu {v} vezes")                      #quantidade de vezes que o usuario venceu
# prints que aconteceram, caso ganhar vai jogar novamente
# se perder é game over








