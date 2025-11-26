times = ("flamengo", "palmeiras", "cruzeiro", "mirassol", "bahia",
         "botafogo", "sao paulo", "bragantino", "corinthians", "fluminense",
         "ceara SC", "internacional", "Atletico MG", "gremio", "vasco", "santos",
         "vitoria", "juventude", "fortaleza", "sport recife")
print(f"os 5 primeiros times sao:{times[0:5]}")
print(f"os 4 ultimos times sao:{times[-4:]}")
print(f"times em ordem alfabetica:{sorted(times)}")
#funcao sorted para colocar em ordem alfabetica, ela nao muda a tupla, pq tuplas sao imutaveis
print(f"o internacional esta na {times.index('internacional')+ 1} posicao")
#funcao index, para encontrar a palavra desejada na tupla!!
