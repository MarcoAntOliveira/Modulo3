import json

class Jogo:
    def __init__(self, nome, ano):
        self.nome = nome  
        self.ano = ano

gears = Jogo("Gears of war", 2012)
god = Jogo("God of war", 2020)
Hori = Jogo("Horizon Zero dwan", 2018)

compras = [gears.__dict__, god.__dict__, Hori.__dict__]

def Fazer_dump():
    with open('jogo.json', 'w', encoding='utf-8') as arquivo:
        json.dump(
            compras,
            arquivo,
            ensure_ascii=False,
            indent=2
    )
