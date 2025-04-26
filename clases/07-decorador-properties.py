"""
Importante cuando queremos validar una propiedad de una clase
"""
class Perro:
    """N/A"""
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        """N/A"""
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        """N/A"""
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre

perro = Perro("hola")
print(perro.nombre)
