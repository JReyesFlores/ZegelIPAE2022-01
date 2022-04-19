# Importamos las funciones definidas en el archivo "operaciones"
# Podemos colocar un alias a la importación con "import {..nombre} as {..alias}"
import operaciones as oper

# Para acceder a las funciones debemos primero acceder a la importación del módulo
oper.multiplicar(15, 4)

# En esta sección solo importamos la función de sumar
# Esto con la finalidad de poder usar dicha función sin hacer una referencia al módulo
from operaciones import sumar

sumar(10, 15)