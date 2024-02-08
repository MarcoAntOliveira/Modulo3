#checa os indices 
#cada vez que o jogador joga , os indices do tabuleiro sao 
# salvos em array dentro do jogador
# se eu tiver os tres indices de colunas ou linhas iguais
# ou os tres indices onde as linhas e colunas sao iguais
# o jogador ganha 



class Jogador:
    def __init__(self):
        self.jogadas = {}
    def jogada(self, pos_y, pos_x):
        self.jogadas[pos_y] = pos_x
