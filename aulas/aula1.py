class Carro:
    def __init__(self, nome = 'seila') -> None:
        self.nome = nome    
    def acelerar(self):
        print(f"{self.nome} está acelarando")

bmw  = Carro("BMW")
bmw.acelerar()


