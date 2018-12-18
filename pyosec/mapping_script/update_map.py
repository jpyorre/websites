import folium
from folium import plugins
import pandas as pd

df=pd.read_csv("joshtravel.txt")
map_osm=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=2)#,tiles='Stamen Toner')
fg=folium.FeatureGroup(name="Josh Travel")
for lat,lon,location in zip(df['LAT'],df['LON'],df['LOCATION']):
	fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.Popup(location))))
	map_osm.add_child(fg)

visitor_lats, visitor_lons = [],[]
heatmap_map = folium.Map(location=[37.804363, -122.271111], zoom_start=2)
data = zip(visitor_lats,visitor_lons)
hm = plugins.HeatMap(data)
heatmap_map.add_child(hm)
map_osm.save('map.html')
