import random
import sys


opción1 = "X"
opción2 = "O"
jugador1 = input("Por favor indique nombre de participante #1: ")
print(jugador1, end = ",")
fichaJ1 = input( " por favor indica con qué ficha deseas jugar: [X] o [O] ")


if fichaJ1 == opción1:
    jugador2 = input("Por favor indique nombre de participante #2:")
    fichaJ2 = "O"
    print(jugador2, ",te toca jugar con la siguiente ficha:", fichaJ2)
elif fichaJ1 == opción2:
    jugador2 = input("Por favor indique nombre de participante #2:")
    fichaJ2 = "X"
    print(jugador2, ",te toca jugar con la siguiente ficha:", fichaJ2)
else:
    print("Opción no valida. Terminando el juego. Vuelva a iniciar el código para volver a jugar.")
    sys.exit() 


print("Lanzando una moneda al aire para determinar quién inicia la partida...")
primerTurno = random.choice([jugador1, jugador2]) 
segundoTurno = [jugador1, jugador2].remove(primerTurno) 
print("La partida la inicia", primerTurno)


tablero = """ 
1234567
+-------+
|.......|
|.......|
|.......|
|.......|
|.......|
|.......|
+-------+
""" ## """ Permite usar multiples filas
S = random.choice([1, 2, 3, 4, 5, 6, 7])  ##Escoge al azar una opción entre las columnas
print(tablero)


## Hay que agregar un ciclo "while" en el futuro para que la acción se repita si sucede la condición del "else"
print(primerTurno, end= ", ")
turnoImpar = input("indica un número de columna o pulsa [S] para tentar a la suerte: ")
if turnoImpar == "S":
    print("Mmm...suerte con eso, se eligió aleatoriamente la columna", S, "para tu ficha")
    print(tablero)
elif turnoImpar == "1" or "2" or "3" or "4" or "5" or "6" or "7":
    print("Haz elegido la columna", turnoImpar)
    print(tablero)
else:
    print("Opción invalida. Elija un número entre las columnas 1 a 7 o pulsa [S] para tentar a la suerte")
    ## Agregar un "return" en el futuro 


## Hay que agregar un ciclo "while" en el futuro para que la acción se repita si sucede la condición del "else"
print(segundoTurno, end = ", ")  ##Relacionar jugador par de forma correcta
turnoPar = input("indica un número de columna o pulsa [S] para tentar a la suerte: ")
if turnoPar == "S":
    print("Mmm...suerte con eso, se eligió aleatoriamente la columna", turnoPar, "para tu ficha")
    print(tablero)
elif turnoPar == "1" or "2" or "3" or "4" or "5" or "6" or "7":
    print("Haz elegido la columna", turnoPar)
    print(tablero)
else:
    print("Opción invalida. Elija un número entre las columnas 1 a 7 o pulsa [S] para tentar a la suerte")
    ## Agregar un "return" en el futuro


## Puntuación



##Multiples turnos después...

print(tablero)

print("¡Felicidades, Cosme Fulanito, has ganado la partida!" )
	
