sexo = input("Digite seu sexo: [M/F]").strip().upper() #primeiro eu pergunto
while sexo != 'M' and sexo != 'F': #aplico a condicao
    print("dados invalidos, digite novamente") #enquanto a condicao nao for aceita
    sexo = input("Digite seu sexo: [M/F]").strip().upper() #vou perguntar de novo ate a resposta ser a que eu quero!
print("sexo validado com sucesso") # caso for a que eu quero, printar validacao!

