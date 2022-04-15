# Se necesita un programa para evaluar los puntajes promedio de los estudiantes. El programa debe
# pedir el nombre del estudiante, seguido de su puntaje único. Los nombres pueden ser ingresados
# en cualquier orden. Ingresando un nombre vacío termina la entrada de los datos.
# Luego se debe emitir una lista de todos los nombres, junto con el puntaje promedio evaluado

nombre_estudiante = 'Default'
lista_estudiantes = []
contador_estudiantes = 0
while(nombre_estudiante.strip() != ''):
    nombre_estudiante = input('Ingrese el nombre del estudiante: ')
    if nombre_estudiante.strip() == '':
        break
    contador_estudiantes += 1
    nota_estudiante = float(input('Ingrese la nota del estudiante: '))
    lista_estudiantes.append(
        {'nombre': nombre_estudiante, 'nota': nota_estudiante})

suma = 0
print('='*50)
print('Lista de Estudiantes y notas')
print('-'*50)
for dic in lista_estudiantes:
    suma += float(dic["nota"])
    print(f'Nombre del estudiante: {dic["nombre"]} - Nota: {dic["nota"]}')
print('='*50)

print(f'Promedio: {suma/contador_estudiantes}',
      f'Cantidad de estudiantes: {contador_estudiantes}', sep='\n')
print('='*50)

# Consideraciones para el ejercicio en el material del curso
# ========================================================
# Clase = {'Jhon': [20, 15, 10], 'Javier': [20, 15, 10], 'Juan': [20, 15, 10]}
# def cargar():
#     data = {}
#     nombre = 'Default'
#     while nombre != '':
#         nombre = input('Ingrese nombre: ').strip()
#         if nombre == '':
#             break
#
#         notas = []
#         nota_x = float(input('Ingrese nota: '))
#         notas.append(nota_x)
#         data[nombre] = notas
#     return data
#
#
# Clase = cargar()
#
# print(Clase)
# 
# if len(Clase) > 0:
#     print("El promedio de las notas ingresados de los alumnos es: ")
#     for nom in sorted(Clase.keys()):
#         suma = 0
#         cnt = 0
#         for punt in Clase[nom]:
#             suma += punt  # De esta manera concatenamos valores como tuplas
#             cnt += 1
#         print(nom, ":", suma/cnt)
