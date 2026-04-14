x= eval(input("digite un numero para x: "))
y=eval(input("digite un numero para y : "))
if x == 0 and y == 0:
    print("indeterminado")
elif y < 0:
    print("error: exponente negativo")
else:
    resultat = 1
    comptador = 0
while y>comptador:

        comptador=comptador + 1
        resultat=x*resultat
        print(resultat)


