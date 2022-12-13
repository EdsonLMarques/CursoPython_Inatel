"""
Vamos ao que interessa, plotar os pontos disponibilizados no lat_lon.txt e suas descrições
    - Um sistema que plote no mapa os pontos disponibilizados
    - O sistema deve ser contruido usando classes e funções.
    - As classes criadas devem estar em arquivos separado
"""
import folium
from LIB import Location

#fluxo principal

# abrir o input
file = open("resolucoes/maps/lat_lon.txt", "r")
data = file.read().split("\n")
List_Points = []
for value in data:
    List_Points.append(value.split(","))
# criar os pontos
ObjectList = []
for i in range(0, len(List_Points[0])):
    if List_Points[0][i] != "" and List_Points[1][i] != "" and List_Points[2][i] != "":
        ObjectList.append(Location(lat=List_Points[0][i], lon=List_Points[1][i], name=List_Points[2][i]))

# Criar um mapa
map = folium.Map(location= [ObjectList[0].lat, ObjectList[0].lon], zoom_start=17)

# plotar os pontos
for point in ObjectList:
    point.Plot(map=map)

# salvar mapa
map.save("map.html")