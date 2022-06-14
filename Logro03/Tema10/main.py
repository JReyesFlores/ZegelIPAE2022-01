try:
    # Creando archivos con estado 'w' y 'r'
    # nombre_archivo: str = 'modelo1.txt'
    # miarchivo = open(nombre_archivo, 'w')
    # miarchivo.write(f'{"*"*50}\n')
    # miarchivo.write("Header\n")
    # miarchivo.write(f'{"*"*50}\n')
    # miarchivo.close()

    # archivo = open('modelo1.txt','r')
    # leer = archivo.read()
    # print(leer)

    archivo = open('modelo1.txt', 'r', encoding='utf-8')
    linea = archivo.readline()
    while linea != '':
        print(linea, end='')
        linea = archivo.readline()
    archivo.close()

except FileNotFoundError as ex:
    print('El archivo indicado no existe.')
