from Torre import Torre
from Apartamento import Apartamento
from Fila import Fila

torreA = Torre("A" , "Rua a, 100" )
torreB = Torre("B" , "Rua b, 150" )

ap01 = Apartamento("101", torreA)
ap02 = Apartamento("102", torreA)
ap03 = Apartamento("103", torreB)
ap04 = Apartamento("104", torreB)
ap05 = Apartamento("105", torreB)

ap01.vaga = 1
ap02.vaga = 2

fila = Fila()
fila.add( ap03 )
fila.add( ap04 )
fila.add( ap05 )

vaga = ap02.vaga
ap02.vaga = None
fila.add( ap02 )
x = fila.remover()
x.vaga = vaga
