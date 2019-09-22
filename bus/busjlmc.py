'Respuesta de los laboratorios de Ironhack_JLMC'
'Laboratorio 2'

#################################### 'BUS' ##########################

from statistics import mean, stdev
import statistics

bus_lleno = False
capacidad = 0
paradas = [(24, 8), (19, 5), (16, 12), (18, 7)]
contador_paradas = 0

for parada in paradas:
    capacidad += parada[0] - parada[1]
    if capacidad > 40:
        bus_lleno = True
        contador_paradas += 1
    elif capacidad <= 40:
        contador_paradas += 1
 
print("\nEl número de paradas en total fueron ", contador_paradas)
print("La capacidad máxima del bus es ", capacidad, "lugares")

data = []
for i, j in paradas:
    data.append(i)
    data.append(j)
print(data)

values = data

promedio = mean(values)
print(f"La capacidad promedio del bus es: {promedio} personas")

desv = stdev(values)
print(f"La desviación estándar es: {desv}")
