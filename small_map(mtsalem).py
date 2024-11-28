# Importing the necessary libraries
import folium
from folium.plugins import Search

# Coordinates for Mount Salem, Jamaica
latitude = 18.4855
longitude = -77.9188

# Create a folium map object centered on Mount Salem with an initial zoom level of 15
mount_salem_map = folium.Map(location=[latitude, longitude], zoom_start=15)

# Add a marker to indicate the location of Mount Salem on the map
folium.Marker(
    location=[latitude, longitude],
    popup="Mount Salem, Jamaica",  # Popup text that appears when the marker is clicked
    icon=folium.Icon(icon="cloud", color="blue")  # Customizing the marker's appearance
).add_to(mount_salem_map)

# Creating a feature group for adding searchable locations (e.g., popular points around Mount Salem)
locations = folium.FeatureGroup(name="Searchable Locations")

# Example locations around Mount Salem (latitude, longitude, name)
example_locations = [
    (18.4836, -77.9167, "Cornwall Regional Hospital"),
    (18.4701, -77.9165, "Montego Bay Cultural Centre"),
    (18.4667, -77.9186, "Sam Sharpe Square"),
    (18.4676, -77.9189, "Montego Bay Civic Centre"),
]

# Adding each example location as a marker to the feature group
for lat, lon, name in example_locations:
    folium.Marker(location=[lat, lon], popup=name).add_to(locations)

# Add the feature group to the map
locations.add_to(mount_salem_map)

# Add a search control to the map, enabling location search based on the markers
Search(
    layer=locations,  # The feature group to search within
    search_label='popup',  # Search based on the popup text
    placeholder='Search for a location...',  # Placeholder text in the search bar
    collapsed=False,  # Display the search bar open by default
).add_to(mount_salem_map)

# Saving the map to an HTML file that can be viewed in a web browser
map_filename = 'mount_salem_map_with_search.html'
mount_salem_map.save(map_filename)

# Displaying the path to the saved file for the user
print(f"Map of Mount Salem with search functionality saved to {map_filename}")
