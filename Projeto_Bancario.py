from Conta_Atributos import Conta
from Conta_Clientes import Base_Dados

base = Base_Dados(1)
conta = Conta(123, "Willian", 100.00, 1000.00)

op = 4

while(op != 0):
    
    id = int(input("Digite o número da sua conta:\n"))
    print("\n{} Seja Bem vindo(a) ao SystemInvest\nEscolha a operação\n".format(base.cliente(id)))
    op = int(input("(1)Sacar\n(2)Depositar\n(3)Extrato\n(0)Sair\n\n"))

    if(op == 1):
        num = float(input("\nDigite o valor que deseja sacar: R$"))
        conta.saque(num)
    elif(op == 2):
        num = float(input("\nDigite o valor que deseja depositar: R$"))
        conta.depositar(num)
    elif(op == 3):
        conta.extrato()
    elif(op == 0):
        print("\nSaindo...")
        exit()
    else:
        print("\nOperação invalida\n")