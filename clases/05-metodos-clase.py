"""N/A"""
class User:
    """N/A"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_json(cls, data):
        """N/A"""
        return cls(name=data["name"], age=data["age"])

datos_usuario = {...}
usuario = User.from_json(datos_usuario)
print(usuario.name)
