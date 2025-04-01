def adios(*numeros):
  print(numeros[0])
  resultado=0
  for numero in numeros:
    resultado += numero
  print(resultado)

# No importa cuantos pongamos siempre seran validos con xargs
adios(1,1,4,5,5,6,7,7,123,2,42,34,23,42,34,2)