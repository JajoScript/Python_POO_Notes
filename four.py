class Coche():
# Estado inicial.
    def __init__(self):
# Propiedades.
        self.__Largo = 250
        self.__Ancho = 120
        self.__Ruedas = 4
        self.__Encendido = False

# Metodos.
    def Arrancar(self, Arrancamos):
        self.__Encendido = Arrancamos

        if self.__Encendido == True:
            Chequeo = self.__Check()

        if self.__Encendido == True and Chequeo == True:
            return "El Coche esta Encendido."

        elif self.__Encendido == True and Chequeo == False:
            return "Algo a fallado!"

        else:
            return "El Coche esta Apagado."
    
    def Estado(self):
        print(f"El Coche tiene un Largo de {self.__Largo}cm.")
        print(f"El Coche tiene un Ancho de {self.__Ancho}cm.")
        print(f"El Coche tiene {self.__Ruedas} Ruedas")

# Metodo encapsulado.
# > Solo puede ser usado de manera interna.
    def __Check(self): #__method(self) : encapsulando el metodo 
        print("Realizando Chequeo...")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "ok"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "ok":
            return True
        else:
            return False

# Instanciando al objeto 1.
coche1 = Coche()

# Aplicando metodos al objeto 1:
coche1.Estado()

print(coche1.Arrancar(True)) # name.method

print(30*"-") # ---------------

# Instanciando al objeto 2.
coche2 = Coche()

# Aplicando metodos al objeto 2:
coche2.Estado()

print(coche2.Arrancar(False))