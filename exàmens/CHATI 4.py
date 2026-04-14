parties = ['PSAO', 'PPa', 'Subtract', 'BOXeo', 'PP', 'Pudimos', 'Restar', 'A', 'PN', 'U']
votes = [45, 23, 6, 3, 8, 9, 10, 11, 15, 10]
p=input("Escribe un partidos: ")
found=False
i=0
while i < len(parties) and not found:
    if parties[i] == p:
        found=True
        print(votes[i])
    else :
        i = i + 1

