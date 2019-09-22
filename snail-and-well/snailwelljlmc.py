'Respuesta de los laboratorios de Ironhack_JLMC'
'Laboratorio 1'

from math import sqrt
from statistics import mean, stdev

pozo = 125
Avancexdia = 30
Caidaxnoche = -20
Serpiente_atrapada = True
dia = 0
Avancetot = 0

Avancereal = Avancexdia + Caidaxnoche

while Serpiente_atrapada:
   Avancetot += Avancereal
   dia += 1
   print(f"La serpiente está en su día número: {dia}")
   if Avancetot >= pozo:
      Serpiente_atrapada = False
      break
print("\nLa serpiente escapó en", dia, "días")

####################### BONUS ##########################
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]

Avancereal = Avancexdia + Caidaxnoche
totalcms = 0
dia = 0
contador = 0
Serpiente_atrapada = True

while Serpiente_atrapada:
    totalcms += advance_cm[contador]
    if totalcms >= pozo:
        Serpiente_atrapada = False
        break
    dia += 1

    totalcms += Caidaxnoche
    if totalcms >= pozo:
        Serpiente_atrapada = False
        break
    contador += 1

print("\nAhora la serpiente escapó en sólo", dia, "días")
print("\nDistancia máxima de la serpiente x día es de: ", max(advance_cm))
print("Distancia mínima de la serpiente x día es de: ", min(advance_cm))
print("Avance promedio de la serpiente x día es: ", mean(advance_cm))
print("Desviación estándar del avance es:", stdev(advance_cm))
