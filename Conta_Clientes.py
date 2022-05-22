class Base_Dados:

    def __init__(self, idconta):
        self.idconta = idconta
        
    def cliente(self, valor):
        self.idconta = valor
        dados = {100 : "Willian", 101 : "Rafaela", 102 : "Andre", 103 : "Juliana", 104 : "Luke"}
        id = dados.get(self.idconta)
        return id
    
    