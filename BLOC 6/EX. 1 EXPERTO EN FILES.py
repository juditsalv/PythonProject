 #recordar escirure la variable de F i hem de crera primer el fitxer de aiport.txt, podses write i el tenques després obres un altre fitxer q serà el de resultats.
f_1 = open('airports.txt', 'w')
F.write(41.3851, 2.1734) # Barcelona
F.write(40.4168, -3.7038) # Madrid
F.write(39.4699, -0.3763) # Valencia
f_1.close()
f_1 = open('airports.txt', 'r')
# La sortida: on guardes el resultat net
f_2 = open('result.txt', 'w')
#ARA HEM DE SEPARAR LES LINEAS.
ignoradas=0
parts=split
