import matplotlib.pyplot as plt
import os

class Airport:
    def __init__(self, icao_code, latitude, longitude):
        self.icao_code = icao_code
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.schengen = False

#STEP1
def IsSchengenAirport(code):
    if not code or len(code) < 2:
        return False
    schengen_prefixes = {
        'LO', 'EB', 'LK', 'LC', 'EK', 'EE', 'EF', 'LF', 'ED', 'LG',
        'EH', 'LH', 'BI', 'LI', 'EV', 'EY', 'EL', 'LM', 'EN', 'EP',
        'LP', 'LZ', 'LJ', 'LE', 'ES', 'LS'}
    return code[:2].upper() in schengen_prefixes

def SetSchengen(airport):
    airport.schengen = IsSchengenAirport(airport.icao_code)

def PrintAirport(airport):
    print("Airport Code:", airport.icao_code)
    print("Latitude:", airport.latitude)
    print("Longitude:", airport.longitude)
    print("Schengen:", airport.schengen)
#suggeriment del catgpt , no la podem realitzar encara pq el code no està definit:
#if not code or len(code) != 4:
    #return False
def ParseCoordinate(coord_str):
    direction = coord_str[0]
    seconds = float(coord_str[-2:])
    minutes = float(coord_str[-4:-2])
    degrees = float(coord_str[1:-4])

    decimal = degrees + minutes/ 60 + seconds/ 3600
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

#step 3
def LoadAirports(airports_file):
    airports = []
    try:
            with open(airports_file, 'r') as F:
                lines = F.readlines()
                for line in lines[1:]:  # Saltem la capçalera
                    parts = line.strip().split()
                    if len(parts) == 3:
                        # Usem el teu ParseCoordinate que ja funciona bé!
                        lat = ParseCoordinate(parts[1])
                        lng = ParseCoordinate(parts[2])
                        # Creem l'objecte Airport
                        ap = Airport(parts[0], lat, lng)
                        SetSchengen(ap)  # Marquem si és Schengen
                        airports.append(ap)
    except FileNotFoundError:
        print("Fitxer no trobat.")
    return airports

#recomendación ia:  except FileNotFoundError:
        #return []

airports = LoadAirports("airports_file")  # carga todos los aeropuertos

for airport in airports:
    SetSchengen(airport)

    def SaveSchengenAirports(airports, filename):
        if not airports:  # lista vacía
            return -1

        # filtrar solo Schengen
        schengen = [a for a in airports if a.schengen]

        if not schengen:  # no hay ninguno
            return -1

        # guardar en fichero
        with open(filename, 'w') as f:
            f.write("CODE LAT LON\n")
            for a in schengen:
                f.write(f"{a.icao_code} {a.latitude} {a.longitude}\n")

        return 0

    # ejecutar
    result = SaveSchengenAirports(airports, "schengen_airports.txt")

    # mensaje
    print("No hay aeropuertos Schengen, no se creó el fichero." if result == -1
          else "Fichero de aeropuertos Schengen creado correctamente.")

def AddAirport(airports, airport):
    """
    Añade un aeropuerto a la lista si no está ya en ella.
    Se considera que un aeropuerto ya está en la lista si el ICAO coincide.
    """
    # Buscar si ya existe un aeropuerto con el mismo código ICAO
    for a in airports:
        if a.icao_code.upper() == airport.icao_code.upper():
            # Ya existe, no lo añadimos
            return False

    # No existe, lo añadimos
    airports.append(airport)
    return True

#####EJEMPLO DE COMO CREAR UN AEROPUERTO.

#airports = LoadAirports("airports_file")  # lista de aeropuertos existentes
# Crear un nuevo aeropuerto
#new_airport = Airport("LEMD", 40.4667, -3.567)
# Intentar añadirlo
#if AddAirport(airports, new_airport):
#    print(f"Aeropuerto {new_airport.icao_code} añadido a la lista.")
#else:
#    print(f"Aeropuerto {new_airport.icao_code} ya estaba en la lista.")

def RemoveAirport(airports, code):

    for i, a in enumerate(airports):
        if a.icao_code.upper() == code.upper():
            # Eliminar aeropuerto de la lista
            del airports[i]
            return 0  # eliminado correctamente
    # Si no se encontró
    return -1

from airport import *
import os

# --- Step 4: probar funciones principales ---
print("=== TEST STEP 4 ===\n")

# 1. Crear un aeropuerto individual
airport = Airport("LEBL", 41.297445, 2.0832941)
SetSchengen(airport)
PrintAirport(airport)

# 2. Cargar aeropuertos desde archivo
airports = LoadAirports("airports_file.txt")

# Marcar Schengen
for a in airports:
    SetSchengen(a)

print(f"\n--- LISTADO AEROPUERTOS ({len(airports)} trobats) ---\n")
for a in airports[:5]: # Mostrem només els 5 primers per no col·lapsar la consola
    PrintAirport(a)

# 3. Añadir aeropuerto
new_airport = Airport("LEMD", 40.4667, -3.567)
SetSchengen(new_airport)
if AddAirport(airports, new_airport):
    print(f"\nAeropuerto {new_airport.icao_code} añadido.")
else:
    print(f"\nAeropuerto {new_airport.icao_code} ya estaba en la lista.")

# 4. Eliminar aeropuerto

if RemoveAirport(airports, "LEMD") == 0:
    print("Aeropuerto LEMD eliminado correctamente.")
else:
    print("Error: Aeropuerto LEMD no encontrado.")

# 5. Guardar Schengen

resultat_save = SaveSchengenAirports(airports, "schengen_airports.txt")
if resultat_save != -1:
    print(f"Fichero Schengen creado con {resultat_save} aeropuertos.")
else:
    print("No hay aeropuertos Schengen, no se creó el fichero.")

print("\nArchivos en carpeta actual:", os.listdir())

def PlotSchengenRatio(airports):
    s_count = sum(1 for a in airports if a.schengen)
    n_count = len(airports) - s_count
    plt.figure(figsize=(6, 6))
    plt.pie([s_count, n_count], labels=['Schengen', 'Altres'], autopct='%1.1f%%')
    plt.title("Proporció Schengen")
    plt.show()