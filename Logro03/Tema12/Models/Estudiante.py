class Estudiante:
    def __init__(self, _dni:str, _nombre:str, _apellidos:str, _edad: int):
        self.Nombre = _nombre
        self.Apellidos = _apellidos
        self.DNI = _dni
        self.Edad = _edad
    
    def __str__(self) -> str:
        return f'DNI: {self.DNI}, Nombre: {self.Nombre}, Apellidos: {self.Apellidos}, edad: {self.Edad}'