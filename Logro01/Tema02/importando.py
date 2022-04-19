# Importamos las funciones definidas en el archivo "operaciones.py"
# Podemos colocar un alias a la importación con "import {..nombre} as {..alias}"
from operaciones import *
import operaciones as oper

# Para acceder a las funciones debemos primero acceder a la importación del módulo
oper.multiplicar(15, 4)

# En esta sección solo importamos la función de sumar
# Esto con la finalidad de poder usar dicha función sin hacer una referencia al módulo
# from operaciones import sumar
# ==================================================================================================================

# En este caso vamos a necesitar invocar cualquier función creada en el archivo "operaciones.py"
# para ello importamos todo el contenido con el "*"

sumar(10, 15)

# Imprimiendo la lista de recursos que a la que tiene acceso la importación enviada
print('Operaciones\n', dir(oper))

# Utilizamos una librería nativa de Python e imprimimos los recursos
import math
print('math\n',dir(math))