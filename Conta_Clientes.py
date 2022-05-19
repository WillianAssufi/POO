from Conta_Atributos import Conta
conta = Conta(123, "Willian", 100.00, 1000.00)

cliente = {123 : conta.extrato(), "Rafaela" : 222}
for names in cliente.values():
    print(names)
