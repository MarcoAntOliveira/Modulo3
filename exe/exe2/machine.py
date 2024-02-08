class machine:
    estados = {
                'encher' : False , 
                'lavar'  : False , 
                'centrifugar' : False,
                'molho': False               
                }
   
    def iniciar(self):
        for chave in  self.estados:
            self.estados[chave]= False
        self.estados['encher'] = True 
        
        for i in range(0, 10):
            print(f'{i}- enchendo')
    def lavar(self):
        for chave in  self.estados:
            if chave == 'encher':
                self.estados[chave]= False
        self.estados['lavar'] = True 
        for i in range(0, 10):
            print(f'{i}- lavando')

    def centrifugar(self):
        for chave in  self.estados:
            if chave == ' lavar' or chave == 'molho':
                self.estados[chave]= False
        self.estados['centrifugar'] = True        
        for i in range(0, 10):
            print(f'{i}- centrifugando')
    def molho(self):
        for chave in  self.estados:
            if chave == 'lavar':
                self.estados[chave]= False
        self.estados['molho'] = True    
        for i in range(0, 10):
            print(f'{i}- No estado de molho espere')

    

brastemp = machine()
processos = {
            0 : brastemp.iniciar(),
            1 : brastemp.lavar(),
            2 : brastemp.centrifugar(),
            3: brastemp.molho(),
            4: brastemp.centrifugar()
            }    
for chave in processos:
    processos.get(chave)