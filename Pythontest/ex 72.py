numeros = ("zero", "um", "dois","tres", "quatro", "cinco","seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove", "vinte")
while True:
    num = int(input("escolha um numero entre 0 e 20: "))
    if 0 <= num <= 20:
        break
    else:
        print("numero invalido, digite novamente!")
print(f"voce digitou o numero {numeros[num]}")



