fr = str(input("digite uma frase:")).strip().upper()
inv = "".join(reversed(fr))
len(fr.replace(" ", ""))
if fr == inv:
    print("sua frase ao contrario é {}\nportanto é um palindromo".format(inv))
else:
    print("sua frase ao contrario é {}, portanto nao e um palindromo".format(inv))



