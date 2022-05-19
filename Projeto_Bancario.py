from Conta_Atributos import Conta

conta = Conta(123, "Willian", 100.00, 1000.00)

op = 5

while(op != 0):
   
    print("\nBem vindo ao SystemInvest\nEscolha a operação\n")
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