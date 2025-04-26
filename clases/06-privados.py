"""NA"""
class Perro:
    """NA"""
    patas = 4
    """NA"""
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def habla(self):
        """NA"""
        print(f"{self.__nombre} dice Guau! con edad {self.edad}")

    @classmethod
    def factory(cls):
        """NA"""
        return cls("Perro feliz", 5)

perro1 = Perro.factory()
perro1.habla()
print(perro1.__dict__) # Podemos acceder a los datos de esta manera.
# print(perro1.__nombre) Esto nos da error por que es privado.
