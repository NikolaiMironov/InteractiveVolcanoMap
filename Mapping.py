import pandas
import folium
from folium.map import Marker

#Data import
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])


#map creation
map = folium.Map(location= [40.431874, -98.525470], zoom_start=5, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
for lt, ln, in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt,ln], icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")