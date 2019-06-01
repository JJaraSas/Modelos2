class Carta:
    def __init__(self, color = None, pinta = None, valor = None):
        self.color = color
        self.pinta = pinta
        self.valor = valor

def imprimir(baraja):
    if len(baraja) == 1:
        return [baraja[0].color] + [baraja[0].pinta] + [baraja[0].valor]
    else:
        print [baraja[0].color] + [baraja[0].pinta] + [baraja[0].valor]
        return imprimir(baraja[1:])

baraja = [Carta("Rojo", True, 10),
          Carta("Negro", True, 5),
          Carta("Negro", False, 8),
          Carta("Rojo", False, 3),
          Carta("Rojo", True, 7),
          Carta("Negro", True, 6),
          Carta("Rojo", False, 11),
          Carta("Rojo", True, 13),
          Carta("Negro", False, 9),
          Carta("Rojo", True, 1)]
    
rojas = filter (lambda carta:carta.color == "Rojo", baraja)

noFiguras = filter (lambda carta:carta.pinta == False, baraja)

valores = map(lambda valor:valor.valor, noFiguras)

suma = reduce (lambda x,y:x+y, valores)

print "Baraja Original:"
print imprimir(baraja)
print ""
print "Cartas rojas:"
print imprimir(rojas)
print ""
print "Cartas rojas que no son figuras:"
print imprimir(noFiguras)
print "Valores:" ,valores 
print "Suma:", suma
