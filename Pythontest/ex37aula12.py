num = int(input("digite um numero inteiro:"))
print("""Escolha uma das bases para conversao:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
opcao = int(input("sua opcao:"))
if opcao == 1:
    print(bin(num))
elif opcao == 2:
    print(oct(num))
elif opcao == 3:
    print(hex(num))
else:
    print("opcao invalida")






