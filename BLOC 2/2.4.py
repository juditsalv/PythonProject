num1= int(input("esciur un numero: "))
num2= int(input("esciur un numero: "))
comptador=0#CUANDO NOS HAGAN CONTAR DEBE HABER SIEMPRE UNA COSA IGUALDADA A O Y OTRA Q VA SUMANDO!!!!
while num1>0 and num2>0:
    d=num1%10
    d2=num2%10
    num1=num1//10
    num2=num2//10
    if d==d2:#el digito se debe igualar no lo sobrante!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        comptador=comptador+1
print("és repeteix :",comptador) #PRINT A FUERA DLE WHILE!!!!!!!!!!!!!!




