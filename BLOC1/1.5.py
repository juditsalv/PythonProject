#Escriu un programa que llegeixi tres nombres enters pel teclat i determini si es compleix la següent propietat: un d'ells és la suma dels altres dos.
# Per exemple, si els nombres introduïts són 7, 21, 14,
# llavors SÍ que es compleix la propietat perquè $21 = 7 + 14$. El programa ha d'escriure un missatge adequat amb la resposta ('els nombres compleixen la propietat').
n1= int(input("Escriu un numero: "))
n2= int(input("Escriu un numero: "))
n3= int(input("Escriu un numero: "))

if n1+n2==n3 or n1+n3==n2 or n1+n3==n2:
    print("els nombres compleixen la propietat")
else:
    print("els nombres no compleixen la propietat")