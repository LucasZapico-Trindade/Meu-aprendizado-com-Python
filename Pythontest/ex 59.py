from time import sleep

num1 = int(input("digite um numero:"))
num2 = int(input("digite outro numero:"))
opcao = 0
soma = num1 + num2
multiplicacao = num1 * num2
maior = 0
while opcao != 5:
    print("""
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa""")
    opcao = int(input("qual e sua opcao?"))
    if opcao == 1:
        soma = num1 + num2
        print("a soma entre {} e {} fica {}".format(num1, num2, soma))
    elif opcao == 2:
        multiplicacao = num1 * num2
        print(" a multiplicacao entre {} e {} fica {}".format(num1, num2, multiplicacao))
    elif opcao == 3:
        if num1 >= num2:
            maior = num1
        elif num2 >= num1:
            maior = num2
        print("entre os valores {} e {} o maior e {}".format(num1, num2, maior))
    elif opcao == 4:
        print("digite novos numeros")
        num1 = int(input("digite um numero:"))
        num2 = int(input("digite outro numero:"))
    elif opcao == 5:
        print("finalizando...")
    else:
        print("opcao invalida, escolha novamente")
    print("=-=" * 10)
    sleep(1)
print("fim do programa")






