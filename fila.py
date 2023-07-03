from Apartamento import Apartamento

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def add(self, apto):
        if self.primeiro == None:
            self.primeiro = apto
            self.ultimo = apto
        else:
            self.ultimo.proximo = apto
            self.ultimo = apto
        self.tamanho += 1
        self.imprimir()
    
    def imprimir(self):
        texto = ""
        if self.primeiro == None:
            texto = "Fila Vazia"
        else:
            aux = self.primeiro
            while( aux ):
                texto += aux.__str__()  
                aux = aux.proximo
        print("-----------")
        print( texto )
        print("-----------")
        print("Total de elementos: ", str(self.tamanho) )
    


    def remover(self):
        aux = self.primeiro
        if self.primeiro == None:
            print("Fila Vazia")
        elif self.primeiro.proximo == None:
            self.primeiro = None
            self.ultimo = None
            self.tamanho = 0
        else:
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
        self.imprimir()
        if aux is not None:
            aux.proximo = None
        return aux
