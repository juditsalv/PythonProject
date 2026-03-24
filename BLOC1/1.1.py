num1 = int(input("Escriba un numero real: "))
num2 = int(input("Escriba un numero real: "))
letra= input("Escriba una letra: ")

if letra=="a":
    suma = num1 + num2
    digito = (suma // 10) % 10
    print("el resultado es ", digito)
elif letra=="b":
    media = (num1 + num2) / 2
    print("el resultado es ", media)
else :
    print("error en el programa")