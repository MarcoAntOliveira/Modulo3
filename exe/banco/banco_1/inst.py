import banco
import pessoa


class Banco:
    def __init__(self, agencias : list[int]| None  = None, clientes: list[pessoa.Pessoa] | None =  None, contas: list[banco.Conta]  = None):
        self.agencias = agencias or []
        self.clientes =clientes or []
        self.contas = contas or []


    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False
        
    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)

            return True
        print('_checa_conta', False)
        return False
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False
    def checa_conta_e_cliente(self, conta, cliente):
        if conta is cliente.n_conta:
            print('_checa_conta e cliente', True)
            return True
        print('_checa_conta e cliente', False)
        return False

    def autenticar(self, cliente :pessoa.Pessoa, conta: banco.Conta):
        return self._checa_agencia(conta) and \
                self._checa_cliente(cliente) and \
                self._checa_conta(conta) and \
                self.checa_conta_e_cliente(cliente, conta)
    def __repr__(self):
        class_name = type(self).__name__
        attrs= f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}, {attrs}'


if __name__ == "__main__":

    p1 = pessoa.Cliente("marcos", 25)
    p1.conta = banco.ContaCorrente(111, 456)

    p2 = pessoa.Cliente("maria", 32)
    p2.conta = banco.ContaPoupança(4532, 645)
    
    banco = Banco()
    banco.clientes.extend([p1, p2])
    banco.agencias.extend([111, 222])
    banco.contas.extend([p1.conta, p2.conta])
    print(banco.autenticar(p1, p1.conta))
    print(banco)