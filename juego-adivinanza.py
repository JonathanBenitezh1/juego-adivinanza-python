
from ast import Break
import random

numero_secreto = random.randint(1,100)
cant_inteentos = 0
intentos_max = 5
adivinado = False

print ("BIENVENIDO AL JUEGO PARA ADIVINAR NUMERO")

while not adivinado:
    if not cant_inteentos < intentos_max:
        print('!GAMER OVER!')
        break

    numero = int(input('INGRESE UN NUMERO: '))

    if numero == numero_secreto:
        print('adivinaste el numero')
        adivinado = True 

    elif numero < numero_secreto:
        print('el numero es mayor')
    else:
        print('el numero es menor')

    cant_inteentos+=1 

          

