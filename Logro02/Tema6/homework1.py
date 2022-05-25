"""
Creamos la clase Alumno y definimos 3 métodos (inicializar,imprimir y mostrar_estado)
Método "inicializar": Crea 2 propiedades para futuras instancias de la clase Alumno.
Método "imprimir": Muestra en consola el nombre y la nota del objeto Alumno.
Método "mostrar_estado": Muestra en consola "Regular" si la nota es mayor o igual a 
                        4, caso contrario mostrará "Libre"
"""


class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def mostrar_estado(self):
        if self.nota >= 4:
            print("Regular")
        else:
            print("Libre")


# bloque principal
alumno1 = Alumno() # Creamos una instancia de la clase Alumno.
alumno1.inicializar("diego", 2) # Asignamos un nombre y una nota al objeto creado
alumno1.imprimir() # Imprimimos lo que tenemos almacenado
alumno1.mostrar_estado() # Imprimimos si es "Regular" o "Libre"

alumno2 = Alumno() # Creamos una segunad instancia de la clase Alumno.
alumno2.inicializar("ana", 10) # Asignamos un nombre y una nota al objeto creado
alumno2.imprimir() # Imprimimos lo que tenemos almacenado
alumno2.mostrar_estado() # Imprimimos si es "Regular" o "Libre"
