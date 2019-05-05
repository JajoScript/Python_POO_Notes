# Programacion orientada a objetos.
#   Teoria.
#   ¿ Que es la programación orientada a objetos?

#   Dos tipos de lenguajes:
#   1. lenguajes de programacion orientados a procedimientos.
#       Fortran, Cobol, Basic, Etc.

#   2. lenguajes de programacion orientados a objetos.
#       C++, Javascript, Python, Java, Etc.


# Vocabulario.
# Clase : Modelo donde se redactan las caracteristicas comunes de un objeto. 
# Objeto, Ejemplar, Instanciar : Ejemplar perteneciente a una clase.
# Modularización : Construccion de modulos que funcionan de manera independiente.
# Encapsulamiento : El funcionamiento de un modulo de un objeto no tiene relacion con otro modulo.
# > Metodos de acceso: Union entre los modulos. 
# > solo se tiene acceso a ciertas caracteristicas accesibles.
# > Nomenclatura del punto : "name.propiedad = valor" && "name.funcion(var)".

# Herencia : 
# Polimorfismo : 

# class : Define la clase.
# Coche() : Define el nombre de la clase.
# largoChasis, anchoChasis, ruedas, enmarcha : Propiedad de la clase Coche.

class Coche():

# propiedades de la clase.
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False    

# > Comportamientos => metodos.
# Para crear un metodo se tiene que crear una funcion.
# def : crea una funcion.
# Arrancar, Estado : nombre de la funcion.
# self : variables por defecto, hace referencia al objeto.
# > self es obligatorio.
# pass : permite que el programa corra a pesar de no haber codigo.

# Comportamiento de la clase.
    def Arrancar(self):
        self.enmarcha = True         

    def Estado(self):
        if self.enmarcha == True:
            return "el Coche esta en marcha"
        else:
            return "el Coche esta parado"

# Crear un objeto. (instanciar una clase)
# objeto : nombre del objeto
# Coche() : nombre de la clase

objeto = Coche()

# Accediendo a las propiedades del objeto.
print(f"el largo del coche es {objeto.largoChasis}") # name.propiedad
print(f"el ancho del coche es {objeto.anchoChasis}") # name.propiedad
print(f"el objeto tiene {objeto.ruedas} ruedas") # name.propiedad

# Accediendo a los metodos del objeto.
objeto.Arrancar() # name.method
# > Arrancar inicia el coche.

print(objeto.Estado()) # name.mothod
# > Estado() pregunta el estado del coche.

# self recibe como parametro al nombre del objeto.
# > objeto.Arrancar = True

print(30*"-")
print("segundo objeto..")

# instancia del segundo objeto.
objeto2 = Coche() 

# Propiedades del segundo objeto.
print(f"el largo del coche es {objeto2.largoChasis}") # name.propiedad
print(f"el ancho del coche es {objeto2.anchoChasis}") # name.propiedad
print(f"el objeto tiene {objeto2.ruedas} ruedas") # name.propiedad

# Estado() del segundo objeto.
print(objeto2.Estado()) # name.mothod
