produtos = ("lapis", 1.00, "borracha", 2.00, "apontador", 2.50, "caneta", 1.50, "livro", 25.00, "caderno", 15.00, "mochila", 80.00)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos] :.<30}", end=" ")
    else:
        print(f"R${produtos[pos] :>3.2f}")

