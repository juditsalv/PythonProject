from airport import *
i=0
airport = Airport("LEBL", 41.297445, 2.0832941)

SetSchengen(airport)
PrintAirport(airport)

i=0
#airports = LoadAirports("airports_file")  # o "airports_file.txt"
#while i<len(airports):
#    PrintAirport(airports[i])
#    i=i+1

print(os.listdir())

from airport import *

airport = Airport("LEBL", 41.297445, 2.0832941)
SetSchengen(airport)
PrintAirport(airport)
LoadAirports("Airports.txt")
PlotAirports(LoadAirports('Airports.txt'))
MapAirports(LoadAirports('Airports.txt'))