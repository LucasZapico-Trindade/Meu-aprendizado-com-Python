seg = float(input("digite um segmento de reta:"))
seg2 = float(input("digite outro segmento de reta:"))
seg3 = float(input("digite mais segmento de reta:"))
if seg + seg2 > seg3 and seg + seg3 > seg2 and seg2 + seg3 > seg:
    print("o comprimento das tres retas forma um triangulo")
else:
    print("o seu comprimento de retas NAO formam um triangulo!:")
