"""
Creamos la clase Persona y definimos 3 métodos (inicializar,imprimir y mayor_edad)
Método "inicializar": Crea 2 propiedades para futuras instancias de la clase Persona.
Método "imprimir": Muestra en consola el nombre y la nota del objeto Persona.
Método "mayor_edad": Muestra en consola si es mayor o menor de edad.
"""


class Persona:
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

    def mayor_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")


# bloque principal
persona1 = Persona() # Creamos la instancia de Persona
persona1.inicializar("diego", 40) # Le asignamos el nombre y  edad
persona1.imprimir() # Imprimimos los datos
persona1.mayor_edad() # Evaluamos si se mayor o menor de edad
