#'''Write a program that calculates the power xy for 2 numbers entered from keyboard
#using a loop of products since xy
#= x*x...*x, up to y-times. Before the loop you should
#verify that the value of y is positive, otherwise the program will stop.
x=int(input("Enter a number : "))
y=int(input("Enter a nuber: "))
contador=1
resultat=x
if y>=0:
    while contador <y:
        contador=1+contador
        resultat=resultat*x
    print(resultat)
else:
    print("Y ha de ser positiu")



