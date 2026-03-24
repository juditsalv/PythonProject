#2. Given a sequence of integers read from the keyboard and finished with the number 0, display in the screen if the
#number is divisor of 1456.
n=int(input("escribe un numero que acabe con el numero 0: "))
while n!=0:
    if 1456%n==0:
        print("se puede dividir por 1456")
    else:
        print("el numero NO es divisible por 1456")
    n=int(input("escribe un numero que acabe con el numero 0: ")) #SUPER IMPORTANT POSSAR AIXO 
print("Programa finalitzat.")