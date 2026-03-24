#Write a program that reads 4 numbers from the keyboard and writes the largest and
#smallest of those numbers on the screen.
n1= int(input("Escriu un numero: "))
n2= int(input("Escriu un numero: "))
n3= int(input("Escriu un numero: "))
n4= int(input("Escriu un numero: "))
gran=n1
petit=n1
if n2 > gran:
    gran = n2
elif n2 < petit:
    petit = n2

# comparar n3
if n3 > gran:
    gran = n3
elif n3 < petit:
    petit = n3

# comparar n4
if n4 > gran:
    gran = n4
elif n4 < petit:
    petit = n4

print("El numero mas grande es:", gran)
print("El numero mas pequeño es:", petit)