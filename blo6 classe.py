file=open("personas.txt", "r")
linea=file.readline()
contenedor_edad=0
while linea != "":
    elementos=linea.split(" ")
    edad=int(elementos[1])
    contadores[edad] = contadores[edad] + 1
    linea = f.readline()
f.close()
i=0
while i <= 100:4

    if contadores[i] > 0:

        if i == 1:
            etiqueta = "año"
        else:
            etiqueta = "años"

        print("Número de personas con " + str(i) + " " + etiqueta + ": " + str(contadores[i]))

    i = i + 1

