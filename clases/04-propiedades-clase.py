"""NA"""
class Perro:
    patas = 4
    """NA"""
    def __init__(self, nombre, edad):
        print(nombre)
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        """NA"""
        print(f"{self.nombre} dice Guau! con edad {self.edad}")

mi_perro1 = Perro("Felipe",10)
mi_perro2 = Perro("Carlos",20)

mi_perro1.habla()
mi_perro2.habla()
print(mi_perro1.patas)
