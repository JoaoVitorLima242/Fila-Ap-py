from Torre import Torre

class Apartamento(Torre):
    def __init__(self, numero, torre):
        self.id = None
        self.numero = numero
        self.torre = torre
        self.vaga = None
        self.proximo = None

    def __str__(self):
        texto  = "\n --------------"
        texto += "\nNumero: " + self.numero
        texto += "\nVaga: " + str(self.vaga)
        texto += "\nEndereco: " + self.torre.endereco
        return texto
