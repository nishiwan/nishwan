import sys

diccionario = {
    "Mercedes": "mcast386@xtec.cat",
    "Rayane": "rayane@rayane.sa",
    "Mohamed": "moha@gmail.com",
    "Jad": "jad@gmail.com",
    "Oriol": "joam@gmail.com",
    "Elias": "hola123@gmail.com",
    "Armau": "arnau@gmail.com",
    "Asdrúbal": "asdrubal@gmail.com",
    "Adrian": "pedrosanchez@asix2.com",
    "Eric": "eric@gmail.com",
    "Emma": "pacosanz@gmail.com",
    "nishwan": "nishwan@gmail.com",
    "Javi": "javi@gmail.com",
    "Novel": "novelferreras49@gmail.com",
    "Bruno": "elcigala@gmail.com",
    "David": "argentino@gmail.com",
    "Judit": "judit@gmail.com",
    "Joao": "joao@gmail.com",
    "Laura": "laura@gmail.com",
    "enrico": "123@gmail.com",
    "Joel": "joelcobre@gmail.com",
    "Aaron": "aaron@gmail.com",
    "Moad": "moad@gmail.com",
}

def obtener_correo_por_nombre(nombre):
    return diccionario.get(nombre)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    nombre_ingresado = sys.argv[1]

    correo_obtenido = obtener_correo_por_nombre(nombre_ingresado)

    if correo_obtenido:
        print(f"El correo electrónico de {nombre_ingresado} es: {correo_obtenido}")
    else:
        print(f"No se encontró un correo electrónico para {nombre_ingresado}")

