expressao = str(input("digite a expressao:"))
lista = []
for simbolo in expressao: # para cada simbolo em expr
    if simb == '(': #se o simbolo for igual a parenteses aberto
        lista.append("(") #adicionar um parentes aberto na lista
    elif simb == ')': # e se o simbolo for um parentes fechado
        if len(lista) > 0: #se a lista for lida e for maior que zero
            lista.pop() # excluir o ultimo item da lista
        else: # caso contrario
            lista.append(")") #adicionar o parentes fechado
            break
if len(lista)  == 0: # se a varredura da lista for vazia
    print("a sua expressao esta valida") #validar a expressao
else:
    print("a sua expressao esta invalida")



