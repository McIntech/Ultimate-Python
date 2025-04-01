"""Calculadora Infinita Mejorada"""

while True:
    DATO = None  # Iniciar DATO con None para evitar resultados inválidos

    INPUT1 = input("""
        ¿Qué operación deseas realizar?
        1. sum (Suma)
        2. res (Resta)
        3. mul (Multiplicación)
        4. div (División)
        5. exit (Salir)
    """).lower()

    if INPUT1 == "exit":
        print("Salimos de la aplicación...")
        break

    # verifica si la variable INPUT1 contiene un valor que esté dentro de la lista
    if INPUT1 in ["sum", "res", "mul", "div"]:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if INPUT1 == "sum":
                print("Realizando suma...")
                DATO = num1 + num2
            elif INPUT1 == "res":
                print("Realizando resta...")
                DATO = num1 - num2
            elif INPUT1 == "mul":
                print("Realizando multiplicación...")
                DATO = num1 * num2
            elif INPUT1 == "div":
                if num2 == 0:
                    print("⚠ Error: No se puede dividir entre cero.")
                    continue  # Volver a pedir una nueva operación
                print("Realizando división...")
                DATO = num1 / num2

            print(f"✅ El resultado de tu operación es: {DATO}")

        except ValueError as e:
            print(f"⚠ Error: Ingresa solo números válidos.{e}")

    else:
        print("⚠ Opción no válida. Intenta de nuevo.")
