#"Escriu el codi d'un programa que llegeixi tres nombres enters pel
# teclat i escrigui un missatge a la pantalla indicant si la multiplicació dels tres nombres és un nombre senar (imparell)."
n1= int(input("Escriu un numero: "))
n2= int(input("Escriu un numero: "))
n3= int(input("Escriu un numero: "))
multi= n1 * n2 *n3
if (multi%2)!=0 and multi>0:
    print("el resultado es impar ", multi)
else:
    print("el resultado  es parell", multi)