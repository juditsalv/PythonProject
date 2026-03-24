# 1. Inici de la seqüència (start sequence)
# No usem input perquè l'enunciat ja ens diu que comencem a 8
n = 8
suma = 0

# 2. Mentre NO arribem al final de la seqüència (435 inclòs)
while n <= 435:
    # 3. Processament element a element (sumar-lo)
    suma = suma + n

    # 4. Obtenir el següent element (incrementar d'1 en 1)
    n = n + 1

print("La suma total és:", suma)