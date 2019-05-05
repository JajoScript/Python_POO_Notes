class Coche():
# Estado inicial.
    def __init__(self):
# Propiedades.
        self.__Largo = 250
        self.__Ancho = 120
        self.__Ruedas = 4 # self.__property : encapsulando la propiedad.
        self.__Encendido = False

# Metodos.
    def Arrancar(self, Arrancamos):
        self.__Encendido = Arrancamos

        if self.__Encendido == True:
            return "El Coche esta Encendido."
        else:
            return "El Coche esta Apagado."
    
    def Estado(self):
        print(f"El Coche tiene un Largo de {self.__Largo}cm.")
        print(f"El Coche tiene un Ancho de {self.__Ancho}cm.")
        print(f"El Coche tiene {self.__Ruedas} Ruedas")
        
# Instanciando al objeto 1.
coche1 = Coche()

# Aplicando metodos al objeto 1:
coche1.Estado()
# > muestra las propiedades del coche 1.

print(coche1.Arrancar(True)) # name.method

print(30*"-") # ---------------

# Instanciando al objeto 2.
coche2 = Coche()

# Modificando valor de propiedades.
coche2.__Ruedas = 3 # name.property = newValue
# > no modifica de manera global la propiedad.
# > si crearamos otro objeto éste tendria 4 ruedas.

# Aplicando metodos al objeto 2:
coche2.Estado() #name.method
# > muestra las propiedades del coche 2.

print(coche2.Arrancar(False)) # name.method

# > Estado Inicial : Estado del objeto al crearlo.
# Constructor = __init__ >> estado inicial

# Encapsular una propiedad.
# __name = Value >> no permite que se cambie el valor