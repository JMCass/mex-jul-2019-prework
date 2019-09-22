'Respuesta de los laboratorios de Ironhack_JLMC'
'Laboratorio 6'

######################## ROBIN HOOD #####################

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

x = 0

while x < len(points):
    j = x + 1
    count_a = 1
    while j < len(points):
        if (points[x][0] == points[j][0] and points[x][1] == points[j][1]):
            count_a += 1
        j += 1   
    if count_a >= 2:
        print(f"\nLa flecha ({points[x][0]}, {points[x][1]}) cayó {count_a} veces en el mismo lugar!") 
        print("Esta flecha pertenece a Robin Hood!")
    x += 1

Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0

for x, y in points:
    if x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    else:
        Q4 += 1

print("\nLa distribución de las flechas por cuandrantes son:")
print(f"\tExisten {Q1} flechas en el cuadrante 1")
print(f"\tExisten {Q2} flechas en el cuadrante 2")
print(f"\tExisten {Q3} flechas en el cuadrante 3")
print(f"\tExisten {Q4} flechas en el cuadrante 4")

'Distancia Euclideana'
from math import sqrt

x = 0

while x < len(points):
    j = x + 1
    while j < len(points):
        result = sqrt((points[x][0] - points[j][0]) ** 2 + (points[x][1] - points[j][1])**2)
        j += 1
        if result == 0:
            print(f"\nLa flecha {x} y la flecha {j} están en el centro: {result}")
    x += 1


cont = 0 
x = 0

while x < len(points):
    j = x + 1
    while j < len(points):
        result = sqrt((points[x][0] - points[j][0]) **2 + (points[x][1] - points[j][1])**2)
        j += 1
        if result == 9:
            cont += 1
            print(f"\n\tLa flecha {x} y la flecha {j} están cercanas a un radio: {result}")
    x += 1

print(f"\nLa cantidad de flechas por recoger son: {cont}")

