# Define clase a partir de Exception
class LongPassw(Exception):
    # Excepción definida por usuario
    def __init__(self, longitud):  # define método constructor ...
        Exception.__init__(self)  # … de excepción ...
        self.longitud = longitud  # … y con atributo longitud

try: # bloque de código a vigilar
    clave = input("Teclear contraseña: ") # introducir una cadena
    if len(clave) < 6: # si longitud de cadena es menor de 6
        raise LongPassw(len(clave)) # llama a excepción de usuario
except LongPassw as lp: # excepción de usuario
    print("LongPassw: Error por longitud: {0}".format(lp.longitud))
else: # se ejecuta si no hay error
    print("No se ha producido error.") # muestra mensaje