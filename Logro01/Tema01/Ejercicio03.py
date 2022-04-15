# Realizar un menú que tenga las siguientes opciones, para poder registrar datos de un padrón
# electoral.
# Opción 1: Adicionar
# Opción 2: Modificar
# Opción 3: Eliminar
# Opción 4: Consultar
# Opción 5: Imprimir

# Si al final da Enter continúa ingresando datos, caso contrario sale del menú. Solo usando funciones.

def patron_elec():  # UNA FUNCION PARA QUE SIRVA DE ENCABEZADO
    print("PATRON ELECTORAL")
    return("................")


def op1(diccionario1):
    print("ADICIONAR")
    # LA VARIABLE a FUNCIONA COMO PALABRA CLAVE
    dni = input("Ingrese el DNI: ")
    while dni in diccionario1:
        print("DNI EXISTENTE\nPOR FAVOR, AGREGAR OTRO")
        # LA VARIABLE a FUNCIONA COMO PALABRA CLAVE
        dni = input("Ingrese el DNI: ")
    lista = []
    nom = input("Ingrese nombre: ")  # LA VARIABLE nom FUNCIONA COMO VALOR1
    lista.append(nom)  # AGREGAMOS DENTRO DE LA LISTA
    # LA VARIABLE ape FUNCIONA COMO VALOR2
    ape = input("Ingrese apellido: ")
    lista.append(ape)  # AGREGAMOS DENTRO DE LA LISTA
    edad = int(input("Ingresar edad: \n"))
    if edad < 99 and edad > 0:
        print("")
    else:
        print("Ingrese su edad real")
        edad = int(input("Ingrese edad: \n"))
    lista.append(edad)
    diccionario1[dni] = lista  # PROCESO DE ADICIÓN

    return("")


def op2(diccionario2):
    print("MODIFICAR")
    lista = []
    dni = input("Ingrese dni: ")
    while dni not in diccionario2:
        print("INGRESE UN DNI EXISTENTE")
        dni = input("Ingrese dni: ")
    print("A CONTINUACIÓN...")
    print("INGRESE LOS DATOS QUE DESEA MODIFICAR")
    nom = input("Ingresar nombre: ")
    lista.append(nom)
    ape = input("Ingrese apellido: ")
    lista.append(ape)
    edad = int(input("Ingrese edad: "))
    if edad > 0 and edad < 99:
        lista.append(edad)
        print("")
    else:
        print("Ultima opción")
        edad = int(input("Ingrese edad: "))
        diccionario2[dni] = lista
    return("")


def op3(diccionario3):
    print("ELIMINAR")
    dni = input("Ingrese dni que desea eliminar: ")
    while dni not in diccionario3:
        dni = input("INGRESE DNI EXISTENTE: ")
        del diccionario3[dni]
    return("")


def op4(diccionario4):
    print("CONSULTA")
    dni = input("Ingrese el dni en consulta: ")
    while dni not in diccionario4:
        dni = input("INGRESE DNI EXISTENTE: ")
    return(diccionario4[dni])


def op5(diccionario5):
    print("IMPRIMIR")
    return(diccionario5)


# _______________PROGRAMA PRINCIPAL________________
print(patron_elec())  # LLAMAMOS A LA FUNCION DEL ENCABEZADO
enter = input("ENTER PARA CONTINUAR")  # ESTA OPCION NOS FACILITARÁ MÁS ADELANTE EL USO CONTINUO DEL PROGRAMA
patron_elect = {}  # PROGRAMA PRINCIPAL - DICCIONARIO VACÍO
while enter == "":
    op = input("Ingrese una opción\n1) Adicionar\n2) Modificar\n3) Eliminar\n4) Consultar\n5) Imprimir\n")
    num=["1", "2", "3", "4", "5"]

    if op == "1":
        print(op1(patron_elect))
    elif op == "2":
        print(op2(patron_elect))
    elif op == "3":
        print(op3(patron_elect))
    elif op == "4":
        print(op4(patron_elect))
    elif op == "5":
        print(op5(patron_elect))

    print("_"*70)
    print("¿Desea continuar: ?")
    enter=input("ENTER PARA CONTINUAR ")

    # while op.isdigit() != True or op not in num:
    #     print("Ingrese un número del 1-5")
    #     op=input("Ingrese una opción\n1) Adicionar\n2) Modificar\n3)Eliminar\n4) Consultar\n5) Imprimir\n")
    #     if op == "1":
    #         print(op1(patron_elect))
    #     elif op == "2":
    #         print(op2(patron_elect))
    #     elif op == "3":
    #         print(op3(patron_elect))
    #     elif op == "4":
    #         print(op4(patron_elect))
    #     elif op == "5":
    #         print(op5(patron_elect))
    #     # else:
    #     # "imposible"
    #     print("______")
    #     print("¿Desea continuar: ?")
    #     enter=input("ENTER PARA CONTINUAR")
