class Coche():
# Propiedades.
    Largo = 250
    Ancho = 120
    Ruedas = 4
    Encendido = False

# Metodos.
    def Arrancar(self):
        self.Encendido = True
    
    def Estado(self):
        if self.Encendido == True:
            return "El Coche esta encendido."
        else:
            return "El Coche esta Apagado."
        
# Instanciando al objeto 1.
coche1 = Coche()

# Mostrar propiedades del objeto 1.
print(f"El Coche 1 tiene un largo de {coche1.Largo}cm")
print(f"El Coche 1 tiene un ancho de {coche1.Ancho}cm")
print(f"El Coche 1 tiene un total de {coche1.Ruedas} ruedas")

# Aplicando metodos al objeto 1.
coche1.Arrancar() # name.method
# > cambia el Estado a True.

print(coche1.Estado()) #name.method
# > muestra el estado del coche.

print(30*"-") # ---------------

# Instanciando al objeto 2.
coche2 = Coche()

# Mostrar propiedades del objeto 2.
print(f"El Coche 2 tiene un largo de {coche2.Largo}cm")
print(f"El Coche 2 tiene un ancho de {coche2.Ancho}cm")
print(f"El Coche 2 tiene un total de {coche2.Ruedas} ruedas")

# Aplicando metodos al objeto 1.
coche2.Arrancar() # name.method
# > cambia el Estado a True.

print(coche2.Estado()) #name.method
# > muestra el estado del coche.