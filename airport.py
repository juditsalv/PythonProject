class Airport:
    def __init__(self, name, code, latitude, longitude):
        self.name = name
        self.code = code
        self.latitude = latitude
        self.longitude = longitude

    def display_info(self):
        return f"{self.name} ({self.code}): {self.latitude}, {self.longitude}"

    @staticmethod
    def plot_airports(airports):
        import matplotlib.pyplot as plt
        latitudes = [airport.latitude for airport in airports]
        longitudes = [airport.longitude for airport in airports]
        plt.scatter(longitudes, latitudes, marker='o')
        plt.title('Airport Locations')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.show()

    @staticmethod
    def map_airports(airports):
        import folium
        if not airports:
            return None
        first_airport = airports[0]
        m = folium.Map(location=[first_airport.latitude, first_airport.longitude], zoom_start=5)
        for airport in airports:
            folium.Marker(
                location=[airport.latitude, airport.longitude],
                popup=airport.display_info()
            ).add_to(m)
        return m
