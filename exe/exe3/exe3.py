class Carro:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano  
        self._fabricante = None
        self._motor = None


    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, motor):
        self._fabricante = motor

    @property
    def motor (self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor


class Motor:
    def __init__(self, nome, tipo):
        self.nome = nome     
        self. tipo = tipo

class Fabricante:
    def __init__(self, nome):
        self.nome =  nome

quatro_tempos = Motor("Weg", "eletrico")
bmw = Fabricante("BMW")
bmw_320i = Carro("BMW", 2015)
bmw_320i.fabricante = bmw
bmw_320i.motor = quatro_tempos            
print(bmw_320i.nome, bmw_320i.motor.nome,bmw_320i.fabricante.nome)

tesla =  Carro("Tesla", 2023)
tesla.motor = quatro_tempos
 