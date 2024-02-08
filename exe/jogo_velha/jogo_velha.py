import numpy as np
from jogador import Jogador


class Tabuleiro:
    def __init__(self):
        self.tab = np.zeros((3, 3),dtype=int)

    def marca(self, pos_x, pos_y):
        self.tab[pos_x, pos_y] =  1

    def mostra_tab(self):
        for row in self.tab:
            print("\n")
            for element in row:
                print(element,  end= '')
                

class Jogo():
    def __ini__(self):
        self.jogador = Jogador()
        self.tabuleiro =  Tabuleiro()

       
    def checa_indice(self):
        count_win = 0
        for pos in self.jogador.jogadas:
            if pos == self.jogador.jogadas[pos]:
                count_win+=1
        if count_win == 3:
            return True
        return False
    
    def checa_coluna(self):
        count_win = 0
        for pos in self.jogador.jogadas:

            if list(self.jogador.jogadas.values()).count(pos)> count_win:
                count_win = list(self.jogador.jogadas.values()).count(pos)
        if count_win == 3:
            return True
        return False

    
    def checa_linha(self):
        count_win = 0
        for pos in self.jogador.jogadas:
            if list(self.jogador.jogadas.keys()).count(pos)> count_win:
                count_win = list(self.jogador.jogadas.keys()).count(pos)
        if count_win == 3:
            return True
        return False 

if __name__ == "__main__":    
    tab = Tabuleiro()
    tab.marca(1, 1)
    tab.mostra_tab()
    jog = Jogador()

