class Persona:
    def __init__(self, nombre=None, edad = None, estadoCiv = None, hijos = None):
        self.nombre = nombre
        self.edad = edad
        self.estadoCiv = estadoCiv
        self.hijos = hijos
        
def imprimir(personas):
    if len(personas) == 1:
        return [personas[0].nombre] + [personas[0].edad] + [personas[0].estadoCiv] + [personas[0].hijos]
    else:
        print [personas[0].nombre] + [personas[0].edad] + [personas[0].estadoCiv] + [personas[0].hijos]
        return imprimir(personas[1:])

personas = [Persona("Andres", 50, "S", 1),
          Persona("Juan", 28, "S", 0),
          Persona("Maria", 42, "C", 3),
          Persona("Raul", 66, "C", 2),
          Persona("Paula", 25, "S", 1),
          Persona("Josefina", 33, "C", 0),
          Persona("Martin", 47, "S", 0),
          Persona("Luisa", 49, "C", 2),
          Persona("David", 38, "C", 4),
          Persona("Julian", 52, "S", 2)]

entre40_60 = filter (lambda persona:persona.edad > 40 and persona.edad < 60, personas)

hijos2 = filter (lambda persona:persona.hijos <= 2 and persona.hijos > 0, entre40_60)

print "Mayores 40 y menores de 60:"
print imprimir(entre40_60)
print ""
print "Maximo 2 hijos:"
print imprimir(hijos2)
print ""
print "Cantidad:", len(hijos2)
