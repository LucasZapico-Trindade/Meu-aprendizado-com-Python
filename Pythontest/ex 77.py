palavras = ("rabiscar", "pardo", "amarelo", "vermelho",
            "verde", "azul", "branco", "preto")
for p in palavras: # o primeiro for vai analisar cada elemento da tupla.
    print(f"\nna palavra {p.upper()} temos: ", end='')
    for letra in p:
        if letra.lower() in "aeiou": #cada item de uma tupla e uma lista tbm, portanto utilizo outro for para analisar cada letra.
            print(letra, end=" ")

# especifico cada vogal que eu quero ver
#e mando printar a letra de acordo com cada palavra.