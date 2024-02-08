"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
import abc
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

class Cliente(Pessoa):
    def __init__(self, nome, idade ,conta) -> None:
        super().__init__(nome, idade )
        self.conta = conta

class Conta(abc.ABC):
    def __init__(self, agencia:int  , n_conta:int , saldo:int ):
        self.agencia =agencia
        self.n_conta =  n_conta
        self.saldo = saldo
        
    @abc.abstractmethod
    def sacar(self, valor):
        pass

    def deposito(self, valor: float) -> None:
        self.saldo += valor
        print(f'voce depositou {valor} seu  saldo é{self.saldo} ')
    
        

class ContaCorrente(Conta):
    def __init__(self, agencia , n_conta, saldo= 0, lim_extra = 0 ):
        super().__init__(agencia, n_conta, saldo)
        self._lim_extra = lim_extra

    def sacar(self, valor: float) -> float:
        valor_pos_saque =  self.saldo - valor
        lim_maximo =  -self._lim_extra
        if valor_pos_saque >= lim_maximo:
            self.saldo-=valor
            return self.saldo 
        print('valor indisponivel para saque')
        return self.saldo
            
        
class ContaPoupança(Conta):
    def __init__(self, agencia , n_conta, saldo):
        super().__init__(agencia, n_conta, saldo)

    def sacar(self, valor: float)-> float:
        valor_pos_saque =  self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo-=valor
            return self.saldo
        print('valor indisponivel para saque')
        return self.saldo
        
class Banco():
    def __init__(self):
        self.clientes = []

    def add_clientes(self, nova_conta):
        self.clientes.append(nova_conta) 

    def verifica_conta(self, conta):
        if conta is not self.clientes:
           raise ValueError(" Essa conta não existe o banco")
        print("Conta existente no banco")   
        

if __name__ == '__main__':
    cp1 = ContaPoupança(570, 890, 0)
    cp1.sacar(1)
    cp1.deposito(4)
    
    cc1 = ContaPoupança(570, 890, 0)
    cc1.sacar(1)
    cc1.deposito(768)