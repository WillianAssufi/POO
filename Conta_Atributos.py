class Conta:

    def __init__(self, numero, titular, saldo, limite):
        #print("Construindo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("\nO saldo do {} é de R${}".format(self.titular, self.saldo))

    def saque(self, valor):
        if (valor <= self.saldo and valor > 0):
            self.saldo -= valor
            print("\nSeu novo saldo é de R${}".format(self.saldo))           
        elif (valor > self.saldo and valor < self.limite):
            print("\nVoce não possui saldo suficiente")
        elif (valor > self.limite):
            print("\nVoce não pode sacar mais do que o seu limite bancário")
    
    def depositar(self, valor):
        if (valor <= 0.0):
            print("\nNão é possivel depositar esse valor")
        else:
            self.saldo += valor
            print("\nSeu novo saldo é de R${}".format(self.saldo))
            
    def transferencia(self, valor):
        pass        
