frase="mi plato"
frase2="mi palto"
lista2=list(frase2)
lista=list(frase)
contador=0
while contador<len(lista):
    lista[contador]=lista2[contador +1]
    lista[contador+1]=lista2[contador]
    contador=contador+2
stn=''.join(lista)
print(stn)







