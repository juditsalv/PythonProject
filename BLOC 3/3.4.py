from operator import truediv

x=[3,5,4,21,15,4,7,7,6,1,5,4]+[0]*88
#primero buscamos el 2ndo 4
contador_4=0
found=False
i=0
while i<100 and not found: #100 SON LOS ELEMENTOS DLE VECTRO!!
    if x[i]==4:
        contador_4=contador_4+1
        if contador_4==2:
            found=True
    if not found:
        #if contador_4=<2:
            #print("otro 4 en la lista")
        i=i+1
if not found:
    print('No hay más repeticiones del numeor 4')
else: #buscamos primer numeor  q no sea 7 y conatmos siente
    i=i+1
    cont7=0
    found=False
    while i<100 and not found:
        if x[i]!=7:#buscamos num q no sea 7
            found=True
        if not found:
            cont7=cont7+1
            i=i+1
    print("Hay ",cont7," sietes seguidos")

