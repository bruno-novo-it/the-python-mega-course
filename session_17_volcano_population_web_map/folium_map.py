import folium
import subprocess
import requests

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

fg = folium.FeatureGroup(name="My Map")

fg.add_child(folium.Marker(location=[-23.59832,-46.64158], popup="Hi, I'm Home", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")

openweb("chrome", ["Map1.html"])