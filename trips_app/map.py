import folium
import requests


#Global Tooltip
tooltip = 'Click For More Info'
m = folium.Map(location=[53.2734, -7.77832031], zoom_start=12)

folium.Marker([53.2734, -7.77832031], popup='<strong>Your Current Location</strong>',tooltip=tooltip).add_to(m)
