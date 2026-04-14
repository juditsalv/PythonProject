#"""scriu un programa que llegeixi una seqüència de números enters positius per teclat un per un. La lectura s'atura quan l'usuari introdueix un 0. El programa ha de dir quina ha estat la ràfega (consecutiva) més llarga del número 9.
#Exemple d'entrada: 5, 9, 9, 2, 9, 9, 9, 9, 1, 0
#Resultat: La ràfega més llarga de 9s és de 4 """""""
num=eval(input("ingrese un numero"))
max_rafega = 0   # Aquí guardem el rècord
actual_rafega = 0 # Aquí comptem la ràfega que estem mirant ara
while num!=0:
    if num==9:
        actual_rafega+=1
        if actual_rafega>max_rafega:
            max_rafega=actual_rafega
    else:
        actual_rafega=0
    num = eval(input("ingrese un numero"))
print("La ràfega més llarga de 9s és de:", max_rafega)


