while True:
    num = int(input("quer ver a tabuada de qual numero?"))
    if num < 0:
        break
    for c in range(1, 11):
        print(f"{num} x {c} = {num*c}")
print("fim do programa")





