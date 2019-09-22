'Respuesta de los laboratorios de Ironhack_JLMC'
'Laboratorio 5'

from statistics import mean, stdev
##################### PROCESSOR TEMPERATURE ###############

temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76,
                  80, 69, 80, 83, 68, 79, 61, 53, 50, 49, 53, 48, 45, 39]
print(f"\nLa temperaturas registradas son: {temperatures_C}")

t_min = min(temperatures_C)
print(f"\nLa temperatura mínima registrada es: {t_min} ºC")

t_max = max(temperatures_C)
print(f"La temperatura máxima registrada es: {t_max} ºC")

result = []
count = 0

for temp in temperatures_C:
    if temp >= 70:
        result.append(temp)
        count += 1
    else:
        count += 0

print(f"\nEn {count} ocasiones la temperatura es >= a 70ºC")
print(f"Estos valores son: {result} ºC")

promedio = mean(temperatures_C)
print(f"\nLa temperatura promedio es: {promedio}ºC")
desv = stdev(temperatures_C)
print(f"La desviación estándar de la temperatura es: {desv}")
del temperatures_C[3]

average = (temperatures_C[2] + temperatures_C[3])/2

print(f"\nLa temperatura promedio entre las 2am y las 4am fue: {average}ºC")
temperatures_C.insert(3, average)
print(f"\nLos nuevos valores de temperaturas son: {temperatures_C}")

F = []
for c in temperatures_C:
    F.append(1.8 * c + 32)
print(f"\nLas temperaturas convertidos a grados Fahrenheit son: {F}")

degree_65 = 0

for t in temperatures_C:
    if average > 65:
        degree_65 += 1
print(f"\nLa temperatura promedio es > a 65ºC en: {degree_65} ocasion(es)")

degree_70 = 0

for t in temperatures_C:
    if t >= 70:
        degree_70 += 1
    else:
        degree_70 += 0
print(f"La temperatura es >= a 70ºC en: {degree_70} ocasion(es)")

degree_80 = 0

for t in temperatures_C:
    if t > 80:
        degree_80 +=1
    else:
        degree_70 += 0
print(f"La temperatura es > a 80ºC en: {degree_80} ocasion(e)s")
        
if degree_65 > 1 or degree_70 > 4 or degree_80 > 1:
    print("La condición es Verdadera y se debe reemplazar el sistema de enfriamiento")
else:
    print("La condición es Falsa y no es necesario reemplazar el sistema de enfriamiento")

data = {'00 am': 33, '01 am': 66, '02 am': 65, '03 am': 62.0, '04 am': 59, '05 am': 60,
        '06 am': 62, '07 am': 64, '08 am': 70, '09 am': 76, '10 am': 80, '11 am': 69,
        '12 pm': 80, '13 pm': 83, '14 pm': 68, '15 pm': 79, '16 pm': 61, '17 pm': 53,
        '18 pm': 50, '19 pm': 49, '20 pm': 53, '21 pm': 48, '22 pm': 45, '23 pm': 39
}

for key, value in data.items():
    if value > 70:
        print(f"\nLas horas donde la temperatura > 70ºC son: {key}")

loop = False
count = 0

i = 1
while i <= len(data):
    for key, value in data.items():
        if value > 70:
            count += 1
        i += 1
        loop = False
        if i == len(data):
            if count == 4:
                print("Son horas consecutivas")
                loop = True
            else:
                print("\nNo son horas consecutivas")

t_minF = min(F)
print(f"\nLa temperatura mínima es: {t_minF} ºF")

t_maxF = max(F)
print(f"La temperatura máxima es: {t_maxF} ºF")

promedioF = mean(F)
print(f"\nLa temperatura promedio es: {promedioF}ºF")
desvF = stdev(F)
print(f"La desviación estándar de la temperatura es: {desvF}")
