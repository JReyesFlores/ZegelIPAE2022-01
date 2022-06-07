try:  # bloque de código a vigilar
    lista = [1, 2, 3, 4, 5, 6]  # define lista
    print(lista)  # muestra lista
    while True:  # bucle infinito hasta error
        print("Elemento a borrar", lista[-1])
        lista.pop()  # borra elemento
        assert len(lista) > 1  # la lista debe tener al menos 2
        print(lista)  # muestra lista después de borrado
        
except AssertionError:  # excepción para assert
    print("Error al intentar borrar elemento")  # mensaje de assert
    print("La lista debe contener al menos 2")
