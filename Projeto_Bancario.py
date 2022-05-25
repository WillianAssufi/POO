from Conta_Atributos import Conta
from Conta_Clientes import Base_Dados

contas = Base_Dados(0)
funcoes = Conta(1000.00, 0)

while True:
    op = 6
    id = int(input("\nDigite o número da sua conta: "))
    contas.senha(id), funcoes.id_atual(id)
    print("\n{} Seja Bem vindo(a) ao SystemInvest\nEscolha a operação\n".format(contas.cliente(id)))

    while(op != 0):
        op = int(input("(1)Sacar\n(2)Depositar\n(3)Extrato\n(4)Transferir\n(5)Deslogar\n(0)Fechar Programa\n\n"))

        if(op == 1):
            valor = float(input("\nDigite o valor que deseja sacar: R$"))
            funcoes.saque(valor)
        elif(op == 2):
            valor = float(input("\nDigite o valor que deseja depositar: R$"))
            funcoes.deposito(valor)
        elif(op == 3):
            funcoes.extrato()
        elif(op == 4):
            valor = int(input("\nPara qual conta deseja transferir: "))          
            valor2 = float(input("\nDigite o valor que deseja transferir: R$"))
            funcoes.transferencia(valor2, valor)
        elif(op == 5):
            print("Deslogando")
            break
        elif(op == 0):
            print("\nFechando...")
            exit()
        else:
            print("\nOperação invalida\n")