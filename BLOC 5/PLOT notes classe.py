import matplotlib.pyplot as plt
#hem de fer 2 plots, un per le snotes i l'altre pels resultats. VRX=["s","a","n","e"] son de suspès,aprobat,.....
#ara hem d efer-ho amb plot d enotes vny=[0]*11 (num notes totals) vnx=[0,1,2,3,4,5,6,7,8,9,10]
vry=[0]*4
vrx=["s","a","n","e"]
vny=[0]*11
vnx=[0,1,2,3,4,5,6,7,8,9,10]
i=0
while i<n:
    if vn[i]<5:
        vry[0] +=1
    elif vn[i]<7:
        vry[1]+= 1
    elif vn[i]<9:
        vry[2]+= 1
    else:
        vry[3]+= 1
vny=[vn[i]]+= 1
i+=1