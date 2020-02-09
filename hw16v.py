"""
Написать программу, которая будет считывать из файла gps координаты,
и формировать текстовое описание объекта и ссылку на google maps.
Пример:

Input data: 60,01';30,19'
Output data:
Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район, Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322
"""
import requests

f1 = open('coord.txt', 'r')
line = f1.readline()
f1.close()
lat, long = line.rstrip().split(";")
lat = float(lat.replace(",", ".").rstrip("'"))
long = float(long.replace(",", ".").rstrip("'"))
coord = {'lat': lat, 'lon': long, 'format':'geocodejson'}
resp = requests.get(f"https://nominatim.openstreetmap.org/reverse", params=coord).json()
location = resp["features"][0]["properties"]["geocoding"]["label"]

print(f"Input data: {line.rstrip()}")
print("Output data:")
print(f"Location: {location}")
print(f"Goggle Maps URL: https://www.google.com/maps/search/?api=1&query={lat},{long}")