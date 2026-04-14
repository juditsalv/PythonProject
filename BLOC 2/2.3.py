lletra = ""
votos_validos = 0
votos_nulos = 0

while lletra != "E":
    votos = input("Enter votos y una letra: ")
    partes = votos.split()

    numvotos = int(partes[0]) #hem d'igualar els num d evotos no podem estar sumat 1 q  ales coses.
    lletra = partes[1]

    if lletra == "V":
        votos_validos += numvotos
    elif lletra == "N":
        votos_nulos += numvotos
    elif lletra == "E":
        break# pq pari
    else:
        continue

votos_total = votos_validos + votos_nulos

if votos_total > 0: #pensar q al estar dividit NO pOT ser menor o igual a =
    porcentaje_validos = votos_validos * 100 / votos_total
    porcentaje_nulos = votos_nulos * 100 / votos_total

    print(f"Válidos: {porcentaje_validos:.1f}%, Nulos: {porcentaje_nulos:.1f}%") #per q posi els resultats