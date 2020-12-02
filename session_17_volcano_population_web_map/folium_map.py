import folium
import subprocess
import requests
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# Open a page with Chrome through Python
#https://pythonprogramming.altervista.org/how-to-open-a-web-page-in-the-browser-using-chrome-with-python-and-webbrowser/
#https://linuxhint.com/execute_shell_python_subprocess_run_method/
import webbrowser

# Open Web Browser
def openweb(browser="", sites=[]):
    # Find Google Chrome instalation Path
    process = subprocess.run(["which", "google-chrome"], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    chrome_path_linux = process.stdout
    if browser == "chrome":
        chromedir = chrome_path_linux
    for site in sites:
        webbrowser.get(chromedir).open(site)

# Get Current Location
def get_current_location():
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    city = data['city']
    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]
    return city,location,latitude,longitude

current_location = get_current_location()

map = folium.Map(location=[current_location[2], current_location[3]], zoom_start=15, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

# Marke Layer
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=folium.Popup(iframe),
        fill_color = color_producer(el), color = "grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

# Json Layer
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())


html_file="Map_html_popup_advanced.html"

map.save(html_file)

openweb("chrome", [html_file])