suma=0
pes=71
while pes < 90:
    imc=pes/(1.80**2)#he de caluclar el im
    suma=suma+imc
    pes=pes+1#avançar d epes a l'hora.
mitjana=suma/20
print(mitjana)