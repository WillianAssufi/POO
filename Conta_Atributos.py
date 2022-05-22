from Conta_Clientes import Base_Dados
contas = Base_Dados(0)
class Conta:

    def __init__(self, saldo, limite, saldoPadrao):
        #print("Construindo objeto ... {}".format(self))
        self.__saldo = saldo
        self.__limite = limite
        self.__saldoPadrao = saldoPadrao

    def saldoAtual(self, valor):
        id = valor    
        dados = {100 : 2000.00, 101 : 1500.00, 102 : 1000.00, 103 : 500.00, 104 : 50.00}
        saldo = dados[id]
        self.__saldoPadrao = saldo
        
    def extrato(self):
        print("\nO saldo da sua conta é de R${:.2f}".format(self.__saldoPadrao))

    def saque(self, valor):
        if (valor <= self.__saldo and valor > 0):
            self.__saldo -= valor
            print("\nSeu novo saldo é de R${:.2f}".format(self.__saldo))           
        elif (valor > self.__saldo and valor < self.__limite):
            print("\nVoce não possui saldo suficiente")
        elif (valor > self.__limite):
            print("\nVoce não pode sacar mais do que o seu limite bancário")
    
    def deposito(self, valor):
        if (valor <= 0.0):
            print("\nNão é possivel depositar esse valor")
        else:
            self.__saldo += valor
            print("\nSeu novo saldo é de R${:.2f}".format(self.__saldo))
            
    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)        

    #def saldoPadrao(self, valor):
    #    dados = {100 : 2000.00, 101 : 1500.00, 102 : 1000.00, 103 : 500.00, 104 : 50.00}
    #    dados.update({})
