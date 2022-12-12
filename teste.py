# passo 2
import folium

mapa = folium.Map(location=[-22.257044861335906, -45.69635809285212], zoom_start=17)
mapa.save("index.html")


"""
O proximo passo é entender como plotar pontos utilizando o folium
para isso vamos utilizar o metodo MARKER que precisa das seguintes informações
    location, popup, tooltip, icon, draggable
Nem todas essas informções sao realmente necessarias.
"""

# passo 3
import folium
lat_lon = [-22.257044861335906, -45.69635809285212]

mapa = folium.Map(location=lat_lon, zoom_start=17)

popup_text = "<i>Inatel</i>"
tooltip_text = "Clique aqui"

folium.Marker(location=lat_lon, popup=popup_text, tooltip=tooltip_text).add_to(mapa)

mapa.save("index.html")

"""
Vamos ao que interessa, plotar os pontos disponibilizados no lat_lon.txt e suas descrições
"""

