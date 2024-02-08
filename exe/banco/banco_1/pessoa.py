import banco
class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,  nome:str):
        self._nome = nome 

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor: int):
        self._idade = valor

    def __repr__(self):
        class_name = type(self).__name__
        attrs= f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}, {attrs}'

class Cliente(Pessoa):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade )
        self.conta: banco.Conta | None = None

if __name__ == "__main__":
   
    p1 = Cliente("marcos", 25)
    p1.conta = banco.ContaCorrente(1234, 456)

    p2 = Cliente("maria", 32)
    p2.conta = banco.ContaPoupança(4532, 645)
    
    print(p2.conta)
    print(p2)