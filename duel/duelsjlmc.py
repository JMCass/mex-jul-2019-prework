'Respuesta de los laboratorios de Ironhack_JLMC'
'Laboratorio 3'
############################ DUEL OF SORCERERS #################

gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

Gandalf_wins = 0
Saruman_wins = 0
Ties = 0 

x = len(gandalf)
y = len(saruman)

for x in range(len(gandalf)):
    if gandalf[x] > saruman[x]:
        Gandalf_wins += 1
    elif gandalf[x] < saruman[x]:
        Saruman_wins += 1
    else:
        Ties += 1

print(f"\nGandalf ganó {Gandalf_wins} veces!")
print(f"Saruman ganó {Saruman_wins} veces!")
print(f"Los hechizeros empataron {Ties} veces")

ganador = False

if Gandalf_wins > Saruman_wins:
    ganador = True
    print("\nEl ganador es Gandalf!")
else:
    ganador = False
    print("\nEl ganador es Saruman!")

print("\n")
############################ BONUS  #################
POWER = {
    'Fireball': 50,
    'Lightning bolt': 40,
    'Magic arrow': 10,
    'Black Tentacles': 25,
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball',
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']

saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles',
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

from statistics import mean, stdev

spell_g = [POWER[j] for j in gandalf]
print(spell_g)

spell_s = [POWER[k] for k in saruman]
print(spell_s)

Gandalf_cwins = 0
Saruman_cwins = 0
Ties = 0
ronda = 0

w = len(spell_g)
z = len(spell_s)

for w in range(len(spell_g)):
    if spell_g[w] > spell_s[w]:
        Gandalf_cwins += 1
        Saruman_cwins = 0
        if Gandalf_cwins >= 3:
            break
    elif spell_g[w] < spell_s[w]:
        Saruman_cwins += 1
        Gandalf_cwins = 0
        if Saruman_cwins >=3:
            break
    ronda += 1

victoria = ronda - 2

print(f"\nEl ganador logró 3 victorias consecutivas de la {victoria}-ta a la {ronda}-va ronda")

if Gandalf_cwins >= 3:
    print("Gandalf es el ganador absoluto!")
elif Saruman_cwins >= 3:
    print("Saruman es el ganador absoluto!")
else:
    print("No hay un ganador!")

print("\nEl poder promedio de los hechizos de Gandalf es: ", mean(spell_g))
print("La desviación estándar de los hechizos de Gandalf es: ", stdev(spell_g))
print("El poder promedio de los hechizos de Saruman es: ", mean(spell_s))
print("La desviación estándar de los hechizos de Saruman es: ", stdev(spell_s))
