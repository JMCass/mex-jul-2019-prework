'Respuesta de los laboratorios de Ironhack_JLMC'
'Laboratorio 4'

########################## Rock, Scissors, Paper ##############################
import math
from random import randint
prompt = "\nPara comenzar a jugar, elige un número entre 1 y N "
prompt += "El número elegido es: "

N = input(prompt)
N = int(N)

valor = N / 2

if valor % 1 == 0:
    valor = int(valor) + 1
    print(f"\nAtención! Al menos debes ganar {valor} de {N} juegos para ser campeón")
elif valor % 2 == 0:
    valor = int(valor) + 1
    print(f"\nAtención! Al menos debes ganar {valor} de {N} juegos para ser campeón")
elif valor % 3 == 0:
    valor = int(valor) + 1
    print(f"\nAtención! Al menos debes ganar {valor} de {N} juegos para ser campeón")
elif valor % 5 == 0:
    valor = int(valor) + 1
    print(f"\nAtención! Al menos debes ganar {valor} de {N} juegos para ser campeón")
else:
    valor = math.ceil(valor)
    print(f"\nAtención! Al menos debes ganar {valor} de {N} juegos para ser campeón")

################## Juego Humano v Computadora
t = ["Piedra", "Papel", "Tijeras"]

player = False
computer = t[randint(0, 0)]

humano = 0
compu = 0
empate = 0

h_pts = 0 * humano
c_pts = 0 * compu
none_pts = 0

i = 1
while i <= N:
    player = input("\n¿Piedra, Papel o Tijeras?: ")
    print(f"\nEste es el juego #{i}")
    if player == computer:
        print(f"\t-Jugador seleccionó {player}")
        print(f"\t-Computadora seleccionó {computer}")
        print("Tenemos un empate!")
        empate += 1
        h_pts += 0
        c_pts += 0
    elif player == "Piedra":
        if computer == "Papel":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Perdiste!", computer, "cubre", player)
            compu += 1
            c_pts += 1
        else:
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Ganaste!", player, "aplasta", computer)
            humano += 1
            h_pts += 2
    elif player == "Papel":
        if computer == "Tijeras":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Perdiste!", computer, "corta", player)
            compu += 1
            c_pts += 1
        else:
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Ganaste!", player, "cubre", computer)
            humano += 1
            h_pts += 2
    elif player == "Tijeras":
        if computer == "Piedra":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Perdiste!", computer, "aplasta", player)
            compu += 1
            c_pts += 1
        else:
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Ganaste!", player, "corta", computer)
            humano += 1
            h_pts += 2
    else:
        i = i -1
        print("Jugada inválida. Revisa tu escritura!")
    i += 1
    
    if i == N:
        if humano or compu > empate:
            player = True
        else:
            player = False
    else:
        player = False

print(f"\nLa cantidad de victorias del humano son: {humano}")
print(f"La cantidad de victorias de la computadora son: {compu}")
print(f"La cantidad de empates son: {empate}")

if humano > compu:
    print('\n¡Humano has ganado!')
    print(f"\tTus puntos acumulados son: {h_pts} puntos del humano")
elif compu > humano:
    print('\n¡Computadora has ganado!')
    print(f"\tLos puntos acumulados son: {c_pts} puntos de la computadora")
else:
    print('\n¡Tenemos un empate!')
    print(f"\tLos puntos acumulados son: {none_pts} puntos para ambos")

######################## BONUS ##########################
prompt = "\nPara comenzar a jugar, elige un número entre 1 y N "
prompt += "El número elegido es: "

N = input(prompt)
N = int(N)

valor = N / 2

if valor % 1 == 0:
    valor = int(valor) + 1
    print(
        f"\nAtención! Al menos debes ganar {valor} de {N} juegos para ser campeón")
elif valor % 2 == 0:
    valor = int(valor) + 1
    print(
        f"\nAtención! Al menos debes ganar {valor} de {N} juegos para ser campeón")
elif valor % 3 == 0:
    valor = int(valor) + 1
    print(
        f"\nAtención! Al menos debes ganar {valor} de {N} juegos para ser campeón")
elif valor % 5 == 0:
    valor = int(valor) + 1
    print(
        f"\nAtención! Al menos debes ganar {valor} de {N} juegos para ser campeón")
else:
    valor = math.ceil(valor)
    print(
        f"\nAtención! Al menos debes ganar {valor} de {N} juegos para ser campeón")

t = ["Piedra", "Papel", "Tijeras", "Lagarto", "Spok"]

player = False
computer = t[randint(0, 4)]

humano = 0
compu = 0
empate = 0

h_pts = 0 * humano
c_pts = 0 * compu
none_pts = 0

i = 1
while i <= N:
    player = input("\n¿Piedra, Papel, Tijeras, Lagarto o Spok?: ")
    print(f"\nEste es el juego #{i}")
    if player == computer:
        print(f"\t-Jugador seleccionó {player}")
        print(f"\t-Computadora seleccionó {computer}")
        print("Tenemos un empate!")
        empate += 1
        h_pts += 0
        c_pts += 0
    elif player == "Piedra":
        if computer == "Papel":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Perdiste!", computer, "cubre", player)
            compu += 1
            c_pts += 1
        else:
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Ganaste!", player, "aplasta", computer)
            humano += 1
            h_pts += 4
    elif player == "Papel":
        if computer == "Tijeras":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Perdiste!", computer, "corta", player)
            compu += 1
            c_pts += 1
        elif computer == "Spok":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Perdiste!", computer, "vence", player)
            compu += 1
            c_pts += 1
        elif computer == "Lagarto":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Perdiste!", computer, "come", player)
            compu += 1
            c_pts += 1
        else:
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Ganaste!", player, "cubre", computer)
            humano += 1
            h_pts += 4
    elif player == "Tijeras":
        if computer == "Piedra":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Perdiste!", computer, "aplasta", player)
            compu += 1
            c_pts += 1
        elif computer == "Spok":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Empate!", computer, "es igual a", player)
            compu += 0
            c_pts += 0
            h_pts += 0
        else:
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Ganaste!", player, "corta", computer)
            humano += 1
            h_pts += 4
    elif player == "Spok":
        if computer == "Piedra":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Perdiste!", computer, "vence a", player)
            compu += 1
            c_pts += 1
        elif computer == "Spok":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Empate!", computer, "es igual a", player)
            compu += 0
            c_pts += 0
            h_pts += 0
        else:
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Ganaste!", player, "corta", computer)
            humano += 1
            h_pts += 4
    elif player == "Lagarto":
        if computer == "Piedra":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Perdiste!", computer, "come", player)
            compu += 1
            c_pts += 1
        elif computer == "Tijeras":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Perdiste!", computer, "corta a", player)
            compu += 1
            c_pts += 1
        elif computer == "Spok":
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Perdiste!", computer, "vence a", player)
            compu += 1
            c_pts += 1
        else:
            print(f"\t-Jugador seleccionó {player}")
            print(f"\t-Computadora seleccionó {computer}")
            print("Ganaste!", player, "come", computer)
            humano += 1
            h_pts += 4
    else:
        i = i - 1
        print("Jugada inválida. Revisa tu escritura!")
    i += 1
    player = False
    if i == N:
        player = True

print(f"\nLa cantidad de victorias del humano son: {humano}")
print(f"La cantidad de victorias de la computadora son: {compu}")
print(f"La cantidad de empates son: {empate}")

if humano > compu:
    print('\n¡Humano has ganado!')
    print(f"\tTus puntos acumulados son: {h_pts} puntos")
elif compu > humano:
    print('\n¡Computadora has ganado!')
    print(f"\tTus puntos acumulados son: {c_pts} puntos")
else:
    print('\n¡Tenemos un empate!')
    print(f"\tLos puntos acumulados son: {none_pts} puntos")
