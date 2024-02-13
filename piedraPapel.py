import random

def jugar_juego(jugador,ordenador):
    opciones = ["piedra", "papel", "tijera"]
    
    if jugador==ordenador:
        return "Empate"
    
    if jugador == "piedra":
        if ordenador == "papel":
            return "Ordenador Gana"
        else:
            return "Jugador Gana"
    
    if jugador == "papel":
        if ordenador == "tijera":
            return "Ordenador Gana"
        else:
            return "Jugador Gana"
        
    
    if jugador == "tijera":
        if ordenador == "piedra":
            return "Ordenador Gana"
        else:
            return "Jugador Gana"
    
    

def main():
    
    jugador = input("Elige piedra papel o tijera:      ")
    
    ordenador = random.choice(["piedra", "papel", "tijera"])
    
    resultado = jugar_juego(jugador,ordenador)
    
    print(resultado)
    
if __name__ == '__main__':
    main()
    