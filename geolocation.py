from folium import Marker
from sunnyday import Weather
from geopy.distance import geodesic
from geopy.geocoders import Nominatim


class Address:

    def __init__(self, area, zone, city, country='India'):
        self.area = area
        self.zone = zone
        self.city = city
        self.country = country

    def coord(self):
        nom = Nominatim(user_agent="Mozilla/5.0")
        address = f"{self.area+', '+self.zone+', '+self.city+', '+self.country}"
        loc = nom.geocode(address)
        return loc


class GeoLoc(Marker):

    def __init__(self, lat, long):
        # Inheriting the parent(Marker) class
        super().__init__(location=[lat, long])
        self.lat = lat
        self.long = long

    def weather(self):
        # Calculates the weather
        weather = Weather(apikey="586f3825fb98b38d0c5719a3f11dc995", lat=self.lat, lon=self.long)
        return weather.next_12h_simplified()


# Calculates the distance
def distance(loc1, loc2):
    return geodesic(loc1, loc2)
