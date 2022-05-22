from Conta_Atributos import Conta
from Conta_Clientes import Base_Dados

contas = Base_Dados(0)
funções = Conta(0, "", 100.00, 1000.00)

op = 4
id = int(input("\nDigite o número da sua conta: "))
contas.senha(id)


while(op != 0):
    
    print("\n{} Seja Bem vindo(a) ao SystemInvest\nEscolha a operação\n".format(contas.cliente(id)))
    op = int(input("(1)Sacar\n(2)Depositar\n(3)Extrato\n(0)Sair\n\n"))

    if(op == 1):
        num = float(input("\nDigite o valor que deseja sacar: R$"))
        funções.saque(num)
    elif(op == 2):
        num = float(input("\nDigite o valor que deseja depositar: R$"))
        funções.depositar(num)
    elif(op == 3):
        funções.extrato()
    elif(op == 0):
        print("\nSaindo...")
        exit()
    else:
        print("\nOperação invalida\n")