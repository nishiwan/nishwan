import random 

intervalo_menor = int(input("introduce el valor menor:  "))
intervalo_mayor = int(input("introduce el valor mayor:  "))




numero = random.randrange(intervalo_menor,intervalo_mayor)
print(numero)
intento = input("Introduce el numero:  ")

if intento < numero:
    print("El numero el mayor")
    if intento > numero:
        print("El numero es menoy")
    else :
        print("Acertaste")

