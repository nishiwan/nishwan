import mysql.connector

def agregar_usuario():
    
    nombre = input("Ingrese el nombre: ")
    email = input("Ingrese el correo electrónico: ")

   
    cursor = connection.cursor()

    try:

        query = "INSERT INTO correos (nombre, email) VALUES (%s, %s)"
        values = (nombre, email)
        cursor.execute(query, values)

  
        connection.commit()

        print("Usuario agregado correctamente.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
       
        connection.rollback()

    finally:
       
        cursor.close()

def buscar_correo():
    
    nombre_buscar = input("Ingrese el nombre para buscar el correo: ")

    
    cursor = connection.cursor()

    try:
        
        query = "SELECT email FROM correos WHERE nombre = %s"
        cursor.execute(query, (nombre_buscar,))

        
        result = cursor.fetchone()

        if result:
            print(f"El correo electrónico para {nombre_buscar} es: {result[0]}")
        else:
            print(f"No se encontró el correo electrónico para {nombre_buscar}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
       
        cursor.close()


connection = mysql.connector.connect(host="localhost", user="root", password="", database="nishwan")

if connection.is_connected():
    print('Conexión exitosa')

    while True:
      
        print("\nMENU:")
        print("1. Agregar usuario")
        print("2. Buscar correo por nombre")
        print("3. Salir")

        opcion = input("Ingrese su opción (1, 2, 3): ")

        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            buscar_correo()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

else:
    print('Fallo en la conexión')


connection.close()
