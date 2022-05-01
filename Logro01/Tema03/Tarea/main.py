# Una sintaxis para importar una o más funciones del módulo creado
# from helper.maths.operations.functions import suma, resta # Importa una o más funciones especificas
# from helper.maths.operations.functions import suma, resta # Importa todas las funciones

# Otra forma de importar
import helper.maths.operations.functions as fns_maths_op
import helper.maths.comparations.functions as fns_maths_cp


try:
    print(f'La suma total es de: {fns_maths_op.suma(10, 15)}')
    print(f'El mayor de los valores: {fns_maths_cp.mayor_valor(8,45,20,1)}')

except Exception:
    print('Error en la aplicación')
