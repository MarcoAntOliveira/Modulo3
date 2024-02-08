from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        self.nome_completo = f'{self.nome}{self.sobrenome}'


if __name__ =="__main__":
    p1 = Pessoa('Luiz', 'Otavio')
    p1.nome_completo ='maria helena'
    print(p1)
    print(p1.nome_completo)