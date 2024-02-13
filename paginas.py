import csv


def cargar_datos(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

mesures_data = cargar_datos("2023_MeteoCat_Detall_Estacions.csv")

metadades_data = cargar_datos("2020_MeteoCat_Estacions.csv")

temperatura_minima = [fila for fila in mesures_data if fila["ACRÒNIM"] == "TM"]

nombre_estacion_map = {(fila["CODI_ESTACIO"], fila["ACRÒNIM"]): fila["NOM_ESTACIO"] for fila in metadades_data}

for medida in temperatura_minima:
    codigo_estacion = medida["CODI_ESTACIO"]
    acronimo = medida["ACRÒNIM"]
    data_lectura = medida["DATA_LECTURA"]
    valor = medida["VALOR"]
    nom_estacio = nombre_estacion_map.get((codigo_estacion, acronimo), "Nombre no encontrado")
    
    print(f"Fecha: {data_lectura}, Temperatura mínima: {valor}, Estación: {nom_estacio}")
