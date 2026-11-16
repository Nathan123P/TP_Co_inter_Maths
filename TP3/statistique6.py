total = 0
temperature = [22, 22.6, 21.1, 21.9, 18.3, 18.7, 21.7, 21.1, 23.6, 27.4, 25.1, 24.9, 23.7, 28.9, 23.2, 26.1, 26.1, 29.8, 28.2, 28.7, 25.9, 26.7, 30.3, 25.2, 21.8, 22, 20.9, 20.7, 20.6, 19.5, 18.8]
for i in range (31) :
        total = total + temperature [i]
moyenne = total/31

Min = temperature[0]
Max = temperature[0]
for i in range (1, len(temperature)) :
    if temperature[i] < Min :
        Min = temperature[i]
    if temperature[i] > Max :
        Max = temperature[i]
Etendue = Max - Min 

print("La moyenne est de "+ str(moyenne))
print("La température maximale  au mois d’août en 2023 est  "+ str(Max))
print("La température minimale  au mois d’août en 2023 est  "+ str(Min))
print("Au mois d’août en 2023 l’étendue de la température était de "+ str(Etendue))
