def largo(texto):
  resultado = 0
  for _ in texto:
    resultado += 1
    return resultado
  
l = largo("hola que tal es mi texto")
print(l)