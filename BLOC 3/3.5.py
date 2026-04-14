frase_str = "Experimentar con xxx a ver que pasa."
frase = list(frase_str)
i = 0

# 1. Recorrem fins a trobar el punt final
while frase[i] != '.':
    if frase[i] == 'x' or frase[i] == 'X':
        # 2. Hem trobat una x! Iniciem el desplaçament (shift)
        j = i
        # Movem TOTS els caràcters una posició a l'esquerra fins al punt
        while frase[j] != '.':
            frase[j] = frase[j + 1]
            j = j + 1

        # --- ERROR CORREGIT AQUÍ ---
        # NO sumem 1 a 'i'. Per què? Perquè la lletra que hem mogut
        # a la posició 'i' podria ser una altra 'x' i l'hem de tornar a revisar.

    else:
        # 3. Si NO és una 'x', passem a la següent lletra
        i = i + 1

# 4. Netegem la "cua" de la llista
# Com que hem mogut el punt a l'esquerra, la llista té lletres repetides al final.
resultat = []
k = 0
while k < len(frase):
    resultat.append(frase[k])
    if frase[k] == '.':  # Parem exactament al primer punt
        break
    k += 1

print('Resultado: ' + ''.join(resultat))




