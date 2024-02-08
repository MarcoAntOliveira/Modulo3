import json
from exe1 import Jogo, Fazer_dump
Fazer_dump()
with open("jogo.json", 'r') as arquivo:
    jogos = json.load(arquivo)
    
    j1 = Jogo(**jogos[0])
    j2 = Jogo(**jogos[1])
    j3 = Jogo(**jogos[2])

    print(j1.nome, j1.ano)
    print(j2.nome, j2.ano)
    print(j3.nome, j3.ano)


