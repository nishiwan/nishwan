import csv

def leer_archivo_csv(ruta):
    with open(ruta, newline='', encoding='utf-8') as archivo:
        datos = {row['NOM']: row['EMAIL'] for row in csv.DictReader(archivo)}
    return datos

def buscar_correo(datos, nombre):
    return datos.get(nombre, "no se encontró")

def main():
    ruta = 'C:/Users/muah1095/Desktop/py/nom-email-ASIX2-2324.csv'
    datos = leer_archivo_csv(ruta)

    persona = input("Nombre de la persona: ")
    correo = buscar_correo(datos, persona)

    print(f"El correo de {persona} es: {correo}")

if __name__ == "__main__":
    main()
