w=input("escribe una palabra: ") #len és la longitud del vector
j=len(w) - 1
i=0
found = False
while (i<len(w)//2) and not found:
    if w[i]!=w[j]:
        found=True
    i= i +1
    j= j-1
if found:
    print("no es polindrómo")
else:
    print(" es polindromo")