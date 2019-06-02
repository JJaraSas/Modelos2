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
