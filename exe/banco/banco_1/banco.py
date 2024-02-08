import abc
 
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
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs= f'({self.agencia!r}, {self.n_conta!r}, {self.saldo!r})'
        return f'{class_name}, {attrs}'

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
    def __repr__(self):
        class_name = type(self).__name__
        attrs= f'({self.agencia!r}, {self.n_conta!r}, {self.saldo!r}, '\
            f'{self._lim_extra!r} )'
        return f'{class_name}, {attrs}'
            
        
class ContaPoupança(Conta):
    def __init__(self, agencia , n_conta, saldo = 0):
        super().__init__(agencia, n_conta, saldo)

    def sacar(self, valor: float)-> float:
        valor_pos_saque =  self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo-=valor
            return self.saldo
        print('valor indisponivel para saque')
        return self.saldo
        
 
if __name__ == '__main__':
    cp1 = ContaPoupança(570, 890, 0)
    cp1.sacar(1)
    cp1.deposito(4)
    
    cc1 = ContaPoupança(570, 890, 0)
    cc1.sacar(1)
    cc1.deposito(768)        