nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
media = (nota1 + nota2) / 2
if media < 5.0:
    print("suas notas foram {} e {}, sua media e de {}, portanto esta reprovado!!".format(nota1, nota2, media))
elif media > 5.0 and media <= 6.9:
    print("suas notas foram {} e {}, sua media e de {}, portanto esta de recuperacao!!".format(nota1, nota2, media))
else:
    print("suas notas foram de {} e {} sua media e {} portanto esta aprovado!!".format(nota1, nota2, media))



