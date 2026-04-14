try:
    numero_original = int(input("Ingrese el número secreto: "))

    # 1. Obtenim el dígit menys significatiu (l'últim)
    ultim_digit = numero_original % 10

    # 2. Calculem la suma de TOTS els dígits
    suma_digits = 0
    temp = numero_original  # Usem una còpia per no perdre el número original

    while temp > 0:
        digit = temp % 10  # Agafem l'últim dígit actual
        suma_digits += digit  # El sumem
        temp = temp // 10  # El eliminem per passar al següent

    # 3. Comprovem la condició de seguretat
    # Primer mirem que l'últim dígit no sigui 0 per evitar errors matemàtics
    if ultim_digit != 0 and suma_digits % ultim_digit == 0:
        print("CONDIÇÃO CUMPLIDA: La suma", suma_digits, "es múltiple de", ultim_digit)
    else:
        print("CONDIÇÃO NO CUMPLIDA")
