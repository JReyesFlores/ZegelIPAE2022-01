# Crear un diccionario en Python que defina como clave el número de documento
# de una persona y como valor un string con su nombre.
# Desarrollar las siguientes funciones:
# - Cargar los datos de 4 personas.
# - Listado completo del diccionario.
# - Consulta del nombre de una persona ingresando su número de documento.
# - Usar funciones.

# Función que genera un diccionario con 4 elementos
def cargar():
    personas = {}
    for x in range(4):
        numero = int(input('Ingrese el número de documento: '))
        nombre = input('Ingrese el nombre: ')
        personas[numero] = nombre
    return personas

# Itera los elementos del diccionario
def imprimir(personas):
    print('Listado del diccionario completo')
    for numero in personas:
        print(numero, personas[numero])

# Filtra el diccionario que se le envíe por argumento
def consulta_por_numero(personas):
    nro = int(input('Ingrese el número de documento a consultar: '))
    if nro in personas:
        print('Nombre de la persona: ', personas[nro])
    else:
        print('No existe una persona con dicho número de documento')

# Verifica si el número ingresado es correcto, esto con el fin de actualizar el valor
# de dicho Key.
def modificar(personas):
    nro = int(input('Ingrese el número de documento a modificar: '))
    if nro in personas:
        nuevo_nombre = input('Ingrese el nuevo nombre: ')
        personas[nro] = nuevo_nombre
        print(f'Se modificó el nombre del documento #{nro} por {personas[nro]}')
    else:
        print('No existe una persona con dicho número de documento')

# Muy similar al actualizar, se verifica la existencia del nro del documento antes
# de eliminar
def eliminar(personas):
    nro = int(input('Ingrese el número de documento a eliminar: '))
    if nro in personas:
        del personas[nro]
        print(f'Se eliminó el documento #{nro}')
    else:
        print('No existe una persona con dicho número de documento')


# bloque principal
personas = cargar() 
imprimir(personas)
consulta_por_numero(personas)
modificar(personas)
eliminar(personas)
imprimir(personas)

