class Base_Dados:

    def __init__(self, idconta):
        self.idconta = idconta
        
    def cliente(self, valor):
        self.idconta = valor
        dados = {100 : "Willian", 101 : "Rafaela", 102 : "Andre", 103 : "Juliana", 104 : "Luke"}
        id = dados.get(self.idconta)
        return id
    
    def senha(self, valor):
        id = valor
        dados = {100 : 1111, 101 : 2222, 102 : 3333, 103 : 4444, 104 : 5555}
        senha = dados[id]
        entrada = 0
        while(entrada != senha):
            entrada = int(input("\nDigite seu PIN de 4 dígitos: "))
            if(entrada == senha):
                break
            else: 
                print("\nPIN incorreto! Tente Novamente...")
            

        
    


        