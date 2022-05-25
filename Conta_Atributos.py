from Conta_Clientes import Base_Dados
contas = Base_Dados(0)
class Conta:

    def __init__(self, limite, id_atual):
        #print("Construindo objeto ... {}".format(self))
        self.__limite = limite
        self.__dados = contas.saldos()
        self.__id_atual = id_atual

    def extrato(self):
        print("\nO saldo da sua conta é de R${:.2f}".format(self.__dados[self.__id_atual]))

    def saque(self, valor):
        if (valor <= self.__dados[self.__id_atual] and valor > 0):
            self.__dados[self.__id_atual] -= valor
            print("\nSeu novo saldo é de R${:.2f}".format(self.__dados[self.__id_atual]))           
        elif (valor > self.__dados[self.__id_atual] and valor < self.__limite):
            print("\nVoce não possui saldo suficiente")
        elif (valor > self.__limite):
            print("\nVoce não pode sacar mais do que o seu limite bancário")
    
    def deposito(self, valor):
        if (valor <= 0.0):
            print("\nNão é possivel depositar esse valor")
        else:
            self.__dados[self.__id_atual] += valor
            print("\nSeu novo saldo é de R${:.2f}".format(self.__dados[self.__id_atual]))
            
    def transferencia(self, valor, destino):
        cliente = contas.cliente(destino)
        id_atual = self.__id_atual
        if(valor > self.__limite):
            print("\nVoce não possui saldo suficiente!\n")
        else:
            self.__dados[id_atual] -= float(valor)
            self.__dados[destino] += float(valor)
            print("\nVoce acabou de transferir R${:.2f} para a conta {:.0f} de {}".format(valor,destino,cliente))

    def id_atual(self, valor):
        self.__id_atual = valor       