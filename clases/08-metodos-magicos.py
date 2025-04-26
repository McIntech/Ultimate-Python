"""N/A"""
class Perro:
    """N/A"""
    def __init__(self, nombre, edad):
        """N/A"""
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Clase perro: {self.nombre}"

    def habla(self):
        """N/A"""
        print(f"{self.nombre} dice Guau!")

perro1 = Perro("Felipe", 7)
perro1.habla()
print(perro1)
