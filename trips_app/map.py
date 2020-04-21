import folium
import requests

r = requests.get('http://192.168.43.25/gps_dashboard.py')
print("what is coming in r", r)

#Global Tooltip
tooltip = 'Click For More Info'
m = folium.Map(location=[53.2734, -7.77832031], zoom_start=12)

folium.Marker([53.2734, -7.77832031], popup='<strong>Your Current Location</strong>',tooltip=tooltip).add_to(m)
