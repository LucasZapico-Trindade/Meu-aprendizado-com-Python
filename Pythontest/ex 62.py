primeiro = int(input("digite o termo: "))
razao = int(input("digite sua razao:"))                            #primeiro de tudo as variaveis!!!!!!!!!!!!
termo = primeiro # contador de termos
cont = 1 #contador de quantidade de termos
total = 0 #total de numeros da PA
mais = 10 # quantidade que o usuario pedir a mais de termos


while mais != 0: # enquanto mais for diferente de 0
    total += mais # total + a quantidade que o usuario digitar
                                                                                #depois impor as condicoes e fazer os calculos
    while cont <= total: #enquanto contador for menor ou igual ao total
        print(f"{termo} -> ", end="") #vou printar os termos pedidos
        termo += razao # calculo da progressao
        cont += 1 #contador pra contar os 10 primeiros termos


    print("pausa")
    mais = int(input("quantos termos voce quer mostrar a mais?"))#pedir mais numeros ao usuario( dentro do while) #pedir de novo, se necessario!!
print(f"progressao finalizada com {total} termos") #mostrar o total de termos