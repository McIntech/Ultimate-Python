"""N/A"""
class Producto:
    """N/A"""
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"

class Categoria:
    """N/A"""
    productos = []
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        """N/A"""
        self.productos.append(producto)

    def imprimir(self):
        """N/A"""
        for producto in self.productos:
            print(producto)

kayak = Producto("kayak", 1000)
bici = Producto("bici", 1000)
longboard = Producto("longboard", 1000)
deportes = Categoria("Deportes", [kayak, bici] )
deportes.agregar(longboard)
deportes.imprimir()
