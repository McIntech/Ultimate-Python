"""Ejercicio"""
def palindromo(texto):
    """Verificar si tenemos un palindromo"""
    texto_sin_espacio = no_space(texto)
    texto_al_revez = texto_reverse(texto_sin_espacio)
    print(texto_sin_espacio, texto_al_revez)
    if texto_sin_espacio.lower() == texto_al_revez.lower():
        print(f'El "{texto}" sí es palíndromo...', True)
    else:
        print(f'El "{texto}" no es palindromo...', False)
    return texto_sin_espacio

def texto_reverse(texto):
    """Iniciar con un reverse para validar"""
    texto_al_reves = ""
    for char in texto:
        print(texto_al_reves)
        texto_al_reves = char + texto_al_reves
    print(texto_al_reves)
    return texto_al_reves

def no_space(texto):
    """Quitando espacio del texto"""
    nuevo_texto = ""
    for char in texto:
        print(char)
        # Quitamos los espacios
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

palindromo("aba")
palindromo("bye")
palindromo("hola que tal")
palindromo("amo la paloma")
