class Cursos:
    def __init__(self, _nombre: str) -> None:
        self.Nombre = _nombre

    def __str__(self) -> str:
        return f'Nombre: {self.Nombre}'