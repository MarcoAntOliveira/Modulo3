from dataclasses import dataclass, asdict, astuple
@dataclass (repr=True,order = True)
class Pessoa:
    nome: str
    sobrenoem:str

if __name__ == "__main__":
    """lista = [ Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista) 
    print(ordenadas)  
"""
    p1 = Pessoa("Marcos", "Anotnio")
    print(asdict(p1))
    print(astuple(p1))