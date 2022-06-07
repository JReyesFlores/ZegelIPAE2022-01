class Invertir:
    def __init__(self, cadena):
        self.cadena = cadena
        self.puntero = len(cadena)

    def __iter__(self):
        return(self)

    def __next__(self):
        if self.puntero == 0:
            raise(StopIteration)
        self.puntero = self.puntero - 1
        return(self.cadena[self.puntero])


# Declara iterable y recorre caracteres
cadena_invertida = Invertir('Iterable')
iter(cadena_invertida)

for caracter in cadena_invertida:
    print(caracter, end=' ')

# Devuelven caracteres que restan por iterar (ninguno):
print(list(cadena_invertida.__iter__()))  # []
