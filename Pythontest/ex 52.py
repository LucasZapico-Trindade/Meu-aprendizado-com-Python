cont = 0
num = int(input("digite seu numero:"))
cont = 0
for primo in range(1, num + 1):
    if num % primo == 0:
        print("\033[1;32m{}".format(primo), end="\033[m ")
        cont += 1
    else:
        print("\033[1;31m{}".format(primo), end="\033[m ")
print("\nO numero {} foi divisivel {} vezes".format(num, cont))
if cont == 2:
    print("por isso ele é primo!!")
else:
    print("por isso ele nao e primo!!")








