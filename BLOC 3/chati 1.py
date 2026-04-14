num = int(input("Ingresa un numero: "))
original = num
x = num
y = 0
while x>0:
    d = x % 10
    y = (y * 10 + d)
    x=x//10
print("El número invertit és:", y)
# 2. Comparem (La manera fàcil)
coincidencies = 0
# Usem 'original' i 'y' per comparar-los d'un en un
while original > 0:
    if (original % 10) == (y % 10):  # Mirem si l'últim dígit de cada un és igual
        coincidencies = coincidencies + 1

    # Els fem petits als dos alhora per mirar el següent dígit
    original = original // 10
    y = y // 10

print("Coincidències:", coincidencies)