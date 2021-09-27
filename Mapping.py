import pandas
import folium
from folium.map import Marker

#Data import
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


#formatting and color chnage of popups
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
def ColorChange(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

#map creation
map = folium.Map(location= [40.431874, -98.525470], zoom_start=5, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanoes")
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln],radius= 7, popup=folium.Popup(iframe), color = ColorChange(el)))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = (open('world.json', 'r', encoding='utf-8-sig').read()), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 
else 'orange' if 10000000 <= x['properties']['POP2005']< 20000000  else 'red'}))

map.add_child(fgv)
#adding layer control panel
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map_adv_popups.html")