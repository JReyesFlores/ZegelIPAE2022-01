from typing import Any
from Models.Estudiante import *

class EstudianteLogic:
    def __init__(self) -> None:
        self.ListaEstudiantes = []

    def __spaceData__(self, data: Any, length: int):
        return str(data)  + ' '*(length-len(str(data)))

    def RegistrarEstudiante(self):
        try:
            dni = input('Ingrese DNI: ')
            nombre = input('Ingrese nombre: ')
            apellidos = input('Ingrese apellidos: ')
            edad = int(input('Ingrese la edad: '))

            est = Estudiante(dni,nombre,apellidos,edad)
            self.ListaEstudiantes.append(est)
            
        except TypeError as ex:
            print('Error en el tipo de dato ingresado.')
        except Exception as ex:
            print(f'Error: \n{ex.args}')
    
    def ListadoEstudiantes(self):
        try:
            print('*'*119)
            print(f'|{self.__spaceData__("DNI", 10)}|{self.__spaceData__("Nombre", 50)}|{self.__spaceData__("Apellidos", 50)}|{self.__spaceData__("Edad", 4)}|')
            print('*'*119)
            for item in self.ListaEstudiantes:
                print(f'|{self.__spaceData__(item.DNI, 10)}|{self.__spaceData__(item.Nombre, 50)}|{self.__spaceData__(item.Apellidos, 50)}|{self.__spaceData__(item.Edad, 4)}|')
            print('*'*119)

        except Exception as ex:
            print(f'Error: \n{ex.args}')
