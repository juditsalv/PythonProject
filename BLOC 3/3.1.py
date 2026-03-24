n=int(input("escribe un numero entero: "))
digito=0
while n!=0:
    if n%2==0:
        n=n//10
        digito=digito+1
        print("todos los numeros son pares")
    else :
         print("el numero no tiene todos los nuemros pares")
    n=int(input("escribe un numero entero: "))