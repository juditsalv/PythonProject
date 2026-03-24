valors_abans=0
valors_despres=0
comptador100=0
n = int(input("Introdueix un número (0 per acabar): "))
 if n == 100:
        comptador100 += 1
    else:
        if comptador100 == 0:
            valors_abans += n
        elif comptador100 >= 3:
            valors_despres += n

    n = int(input("Número (0 per acabar): "))

# fuera del bucle
if valors_abans > valors_despres:
    print("La suma abans és més gran")
else:
    print("No ho és")
