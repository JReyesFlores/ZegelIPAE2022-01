stack = []  # Creamos una lista vacia


def main():  # Creamos un método Main
    print("1 Aplilar elemento (entero)")  # Imprimimos en pantalla la opción 1
    print("2 Desapilar elemento")  # Imprimimos en pantalla la opción 2
    print("3 Mostrar pila")  # Imprimimos en pantalla la opción 3
    print("4 Salir")  # Imprimimos en pantalla la opción 4
    option = input("Elija una opcion: ")  # Se solicita una opción

    # Esta opcion permite apilar el numero en la lista
    if str(option) == "1":  # Evaluamos si la opción ingresada es "1"
        # Se solicita un número
        elemento = input(" Introduzca el numero a apilar: ")
        stack.append(elemento)  # Agrega lo ingresado en la última posición
        print(" Elemento apilado ")  # Muestar mensaje "Elemento apilado"
        main()  # Se utiliza recursión del método main

    # Esta opcion saca desapila a partir del ultimo numero ingresado
    elif str(option) == "2":  # Evaluamos si la opción ingresada es "2"
        if len(stack) == 0:  # Evalua si no existen elementos en la pila
            # Muestar mensaje "No hay elementos para desapilar"
            print(" No hay elementos para desapilar ")
            main()  # Se utiliza recursión del método main
        else:
            # Elimina el último elemento de la pila
            print("El numero: ", stack.pop(), " fue desapilado")
            main()  # Se utiliza recursión del método main

    # Esta opcion imprime en pantalla la pila
    elif str(option) == "3":  # Evaluamos si la opción ingresada es "3"
        # realiza un recorrido de los indices de la pila, iniciando por el último
        for i in reversed(range(len(stack))):
            print("Pila: ", stack[i])  # Imprime el elemento
        main()  # Se utiliza recursión del método main

    # Esta opcion permite salir de la ejecucion del codigo
    elif str(option) == "4":  # Evaluamos si la opción ingresada es "4"
        exit()  # Finaliza el programa
    else:
        # Muestra un mensaje de opción incorrecta
        print("\nOpcion incorrecta.\n")
        main()  # Se utiliza recursión del método main


main()  # Invocamos al método main
