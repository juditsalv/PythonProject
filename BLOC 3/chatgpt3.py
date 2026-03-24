n = int(input("Escribe un número: "))

i = 1
contador = 0

while i <= n and contador < 3:

    if n % i == 0:
        print("Divisor:", i)
        contador = contador + 1

    i = i + 1

if contador < 3:
    print("No hay 3 divisores")