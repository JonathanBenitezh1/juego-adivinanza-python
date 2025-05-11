
nombre1 = input('Nombre jugador 1? : ')
nombre2 = input('Nombre jugador 2? : ')

jugador1 =input ('Hola ' + nombre1+' que elejiras? :')
jugador2 = input ('Hola '+nombre2+' que elejiras? :')

condicion1 = jugador1 == "piedra" and jugador2== "papel"
condicion2 = jugador1 =="papel" and jugador2== "tijera"
condicion3 = jugador1 == "tijera" and jugador2=="piedra"

if jugador1 == jugador2:
    print("ESTO ES UN EMPATE")
elif condicion1 or condicion2 or condicion3:
    print("GANADOR ", nombre2)
else:
    print("GANADOR", nombre1)
