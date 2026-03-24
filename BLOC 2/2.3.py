# Inicialitzem acumuladors
vots_valids = 0
vots_nuls = 0

# 1. Llegim la primera línia (Inici de la seqüència)
entrada = input("Introdueix vots i lletra (ex: 5 V) o '0 E' per acabar: ")
dades = entrada.split() # Separem "5" de "V"

# 2. La condició de final és que la LLETRA (dades[1]) sigui 'E'
while dades[1] != "E":
    try:
        num_vots = int(dades[0]) # Convertim el text "5" en número 5
        lletra = dades[1]        # La lletra és "V" o "N"

        # 3. Processament element a element
        if lletra == "V":
            vots_valids = vots_valids + num_vots
        elif lletra == "N":
            vots_nuls = vots_nuls + num_vots
        # Si és una altra lletra, l'enunciat diu que s'ignora (no fem res)

    except (ValueError, IndexError):
        print("Format incorrecte, línia ignorada.")

    # 4. MOLT IMPORTANT: Tornar a demanar dades (Obtenir següent element)
    # Si no fas això, el bucle mai s'aturarà!
    entrada = input("Següent línia: ")
    dades = entrada.split()

# Càlcul final (fora del bucle)
total = vots_valids + vots_nuls
if total > 0:
    perc_v = (vots_valids / total) * 100
    perc_n = (vots_nuls / total) * 100
    print(f"Vàlids: {perc_v:.1f}%, Nuls {perc_n:.1f}%")