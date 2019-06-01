class Persona:
    def __init__(self, nombre=None, genero = None, cargo = None, salario = None):
        self.nombre = nombre
        self.genero = genero
        self.cargo = cargo
        self.salario = salario
        
def imprimir(personas):
    if len(personas) == 1:
        return [personas[0].nombre] + [personas[0].genero] + [personas[0].cargo] + [personas[0].salario]
    else:
        print [personas[0].nombre] + [personas[0].genero] + [personas[0].cargo] + [personas[0].salario]
        return imprimir(personas[1:])

personas = [Persona("Andres", "M", "Ejecutivo", 950000),
          Persona("Juan", "M", "Operativo", 750000),
          Persona("Maria", "F", "Ejecutivo", 980000),
          Persona("Raul", "M", "Ejecutivo", 850000),
          Persona("Paula", "F", "Operativo", 680000),
          Persona("Josefina", "F", "Ejecutivo", 790000),
          Persona("Martin", "M", "Ejecutivo", 930000),
          Persona("Luisa", "F", "Operativo", 730000),
          Persona("David", "M", "Operativo", 700000),
          Persona("Julian", "M", "Ejecutivo", 870000)]


mujeres = filter (lambda persona:persona.genero == "F", personas)

hombres = filter (lambda persona:persona.genero == "M", personas)

salMuj = map(lambda persona:persona.salario, mujeres)

salHom = map(lambda persona:persona.salario, hombres)

totalMuj = reduce (lambda x,y:x+y, salMuj)

totalHom = reduce (lambda x,y:x+y, salHom)

print "Personas:"
print imprimir(personas)
print ""
print "Hombres:"
print imprimir(hombres)
print ""
print "Mujeres:"
print imprimir(mujeres)
print ""
print "Salarios de hombres:" ,salHom 
print "Salarios de mujeres:", salMuj
print "Total hombre:", totalHom
print "Total mujeres:", totalMuj
