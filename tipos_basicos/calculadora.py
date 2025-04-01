"""Calculadora"""

RESULT = None

option = int(input("""
¿Qué deseas realizar? (Escribe un número):
1: Suma
2: Resta
3: División
4: Multiplicación
"""))

if option == 1:
    RESULT = int(input("Ingrese el primer número: ")) + int(input("Ingrese el segundo número: "))
elif option == 2:
    RESULT = int(input("Ingrese el primer número: ")) - int(input("Ingrese el segundo número: "))
elif option == 3:
    RESULT = int(input("Ingrese el primer número ")) / int(input("Ingrese el segundo número: "))
elif option == 4:
    RESULT = int(input("Ingrese el primer número ")) * int(input("Ingrese el segundo número: "))
else:
    print("No es valido el dato que ingresate...")

print(f"El resultado es: {RESULT}")
