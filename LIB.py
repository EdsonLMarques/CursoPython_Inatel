import folium

class Location:
    def __init__(self, name: object, lat: object, lon: object) -> object:
        self.name = name
        self.lat = lat
        self.lon = lon
    def Plot(self, map):
        folium.Marker(location= [self.lat, self.lon], tooltip=self.name).add_to(map)