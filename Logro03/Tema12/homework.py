from BusinesLogic.EstudianteLogic import *

def salir():
    exit()

def main():
    estLogic = EstudianteLogic()
    
    while True:
        print("\n")
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|         Menu         |**|")
        print("|****************************|")
        print("")
        print("Seleccione una de las siguientes opciones:");
        print("1.- Registrar Estudiante")
        print("2.- Mostrar Estudiantes")
        print("3.- Buscar Estudiante")
        print("4.- Modificar notas")
        print("5.- Consultar Historial")
        print("6.- Salir\n")

        opcion = int(input("Opcion: "))
        if opcion == 1:
            estLogic.RegistrarEstudiante()
        elif opcion == 2:
            estLogic.ListadoEstudiantes()
        elif opcion == 3:
            print('buscarEstudiante()')
        elif opcion == 4:
            print('modificarNotas()')
        elif opcion == 5:
            print('consultarHistorial()')
        elif opcion == 6:
            salir()

if __name__ == '__main__':
    main()