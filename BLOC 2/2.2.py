n=int(input("Enter a number : "))
sum=0
while n>0:
    d=n%10
    n=n//10
    sum=sum+d
    print(sum)
except ValueError:
    print("Error: no es un numero")