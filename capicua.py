igual, posicion = 0, 0

texto = input("Ingrese la palabra: ")

for ind in reversed(range(0, len(texto))):
  if texto[ind]== texto[posicion]:
    igual += 1
  posicion += 1

if len(texto) == igual:
  print("El texto es palindromo")
else:
  print("El texto no es palindromo")