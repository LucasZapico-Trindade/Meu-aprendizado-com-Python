n = int(input("digite o numero: ")) # perguntar ao usuario o numero
t1 = 0 #vai comecar em 0
t2 = 1# o proximo sera 1
print(f"{t1} -> {t2}", end="") #printar os dois em SEQUENCiA
cont = 3 #contador iniciou em 3 porque os 2 primeiros ja temos
while cont <= n: #enquanto o contador for menor ou igual ao numero digitado pelo usuario
    t3 = t1 + t2 #criar uma variavel t3 que vai ser a soma do t1 e o t2
    print(f" -> {t3}", end="") #mostro o t3 na tela
    t1 = t2 #transformando o t1 no t2 ele vai ir pra frente pra criar a sequencia
    t2 = t3 #o mesmo se aplica aqui
    cont += 1 #coloco o contador +1 para ele contar a quantidade que eu pedir




