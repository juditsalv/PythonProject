vn= [0]*10 #estas indican que hi caben 10 notes dins la llista
n=0 #estas indicant que encara no hi han notes a l'inici
nota=int(input("escriba su nota: "))
#num de notes que poden entrar esta indefinit.
while nota!=-1 and n<len(vn): #len es la longitud del vector.
    vn[n]=nota
    n=n+1
    nota=int(input("escriba su nota: "))

if nota==-1 or n==len(vn):
        print("su notas ya se han registrado ")
        print(vn)