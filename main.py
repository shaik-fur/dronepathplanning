import folium
from folium import Map, Popup, PolyLine
from geolocation import GeoLoc, distance, Address
import pandas as pd

# Input address of first location
area = input()
zone = input()
city = input()
country = input()

# Input address of second location
area1 = input()
zone1 = input()
city1 = input()
country1 = input()

# Instantiating the Address class
loc1 = Address(area, zone, city, country)
loc2 = Address(area1, zone1, city1, country1)

# Get the latitude and longitude values and instantiate the geoLoc class
geo = GeoLoc(loc1.coord().latitude,  loc1.coord().longitude)
geo2 = GeoLoc(loc2.coord().latitude, loc2.coord().longitude)

# Initializing the map
mymap = Map(location=[geo.lat, geo.long])

# Generate popup for first marker
popup = Popup(str(geo.weather()))
popup.add_to(geo)

# Generate popup for second marker
popup2 = Popup(str(geo2.weather()))
popup2.add_to(geo2)

# create a list of location
points = [(geo.lat, geo.long), (geo2.lat, geo2.long)]

# Draw line between two points
line = PolyLine(points, color='red', weight='2.5', opacity=1)
line.add_to(mymap)

# Adding markers to specified locations
geo.add_to(mymap)
geo2.add_to(mymap)

# Calculate the distance between two points in Kilometers
print("Distance between two locations is: "+str(distance((geo.lat, geo.long), (geo2.lat, geo2.long)).kilometers))

# Pandas to read csv
df = pd.read_csv('ornagezone.csv')
df2 = pd.read_csv('redzone.csv')

# Adding Polygonal zones
lis = []
for _, row in df.iterrows():
    lis += [[row['lat'], row['long']]]

folium.Polygon(locations=lis, color='orange', fill=True, fill_color='orange', popup='special zone').add_to(mymap)

# Adding red zones
for _, row in df2.iterrows():
    folium.CircleMarker(location=(row['lat'], row['long']),
                        radius=50, color='red',
                        fill=True, fill_color='red').add_to(mymap)

# Saving the map
mymap.save("location.html")
