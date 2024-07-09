

import random


numero_secreto=random.randint(1,101)
cant_intentos=0
cant_max_intentos=5
adivinado=False

print("¡Bienvenide al juego de adivinar el número!")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("Game over, pues no lo hiciste con 5 intentos")
        break
    
    numero=int(input("Introduce un número del 1 al 100: "))

    if numero==numero_secreto:
        print("Felicidades, la pegaste!")
        adivinado=True      
    elif numero<numero_secreto:
        print("No, es mayor!")
    else:
        print("No, es menor!")

    cant_intentos+=1