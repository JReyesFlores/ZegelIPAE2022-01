lista = [10, 100, 1000, 10000]
iterador = iter(lista)
try:
    while True:
        print(F'{iterador.__next__()}')
except StopIteration:
    print("Se ha alcanzado el final de la lista")
