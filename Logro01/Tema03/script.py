# importamos la función "saludar" desde el sub-paquete "hola" que a su 
# vez se encuentra en el paquete llamado "paquete".
from paquete.hola.saludos import saludar
from paquete.adios.despedidas import Despedida

saludar()
Despedida()

# cabe mencionar que es importante ubicar la ubicación de este archivo
# "script.py" pues dependendiendo del nivel en el que se encuentre empezaremos a
# llamar los paquetes y sub-paquetes.
