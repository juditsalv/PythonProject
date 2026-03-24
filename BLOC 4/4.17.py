V=[25, 12, 7, 9, 10, 1, 81, 13]
i=0
lv=len(V)
while i<lv :
    if V[i]%3==0:
        j=i
        while j<lv-1:
            V[j]=V[j+1]
            j=j+1
        lv=lv-1
    else:
        i=i+1

print(V)