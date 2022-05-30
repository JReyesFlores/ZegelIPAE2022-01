"""
Creamos la clase Triangulo y definimos 4 métodos (inicializar, imprimir, lado_mayor
y es_equilatero)
Método "inicializar": Crea 3 propiedades para futuras instancias de la Triangulo.
                        Así mismo es solicitado por teclado que se ingresen valores
                        númericos para estas 3 propiedades.
Método "imprimir": Muestra en consola los datos ingresados al crear la instancia.
Método "lado_mayor": Evalua la información ingresada para obtener el lado mayor.
Método "es_equilatero": Evalua la información ingresada para verificar si es un
                        Triangula equilatero.
"""


class Triangulo:
    def inicializar(self):
        self.lado1 = int(input("Ingrese primer lado: "))
        self.lado2 = int(input("Ingrese segundo lado: "))
        self.lado3 = int(input("Ingrese tercer lado: "))

    def imprimir(self):
        print("Valores de los lados del triángulo: ")
        print("Lado 1: ", self.lado1)
        print("Lado 2: ", self.lado2)
        print("Lado 3: ", self.lado3)

    def lado_mayor(self):
        print("Lado mayor")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(self.lado1)
        else:
            if self.lado2 > self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)

    def es_equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("El triángulo es equilátero")
        else:
            print("El triángulo no es equilátero")


# bloque principal
triangulo1 = Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.es_equilatero()
