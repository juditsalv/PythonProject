#Escriu un programa que llegeixi un número que representi un any pel teclat i indiqui si aquest any és de traspàs (bixest) o no.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100, en aquest cas per ser de traspàs també ha de ser divisible per 400.
año=int(input("Escria un año: "))
#if año%4==0 or año%400==0 :
    #print("el año es bisiesto")
#elif año%100!=0 :
    print("No es un año bisiesto")
#else:
    #print("No es un año bisiesto")
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("És un any de traspàs")
else:
    print("No és un any de traspàs")