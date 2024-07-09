print("¡Este es el piedra, papel o tijera en 3 intentos!")

nombre1=input("¿Cómo se llamará el jugador 1? ")
nombre2=input("¿Cómo se llamará el jugador 2? ")

rondas=0
rondas_max=3

while rondas<=3:
    if rondas==rondas_max:
       print("Se jugaron las 3 rondas")
       break

    jugador1=input("Hola "+nombre1+"! Qué elegís: piedra, papel o tijera?: ")
    jugador2=input("Hola "+nombre2+"! Qué elegís: piedra, papel o tijera?: ")

    condicion1=jugador1.lower()=="piedra" and jugador2.lower()=="tijera"
    condicion2=jugador1.lower()=="papel" and jugador2.lower()=="piedra"
    condicion3=jugador1.lower()=="tijera" and jugador2.lower()=="papel"

    if jugador1==jugador2:
        print("Ha sido un empate!")
        juego=False
    elif condicion1 or condicion2 or condicion3:
        print("Ha ganado "+nombre1+"!")
    else:
        print("Ha ganado "+nombre2+"!")

    rondas+=1