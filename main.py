import requests
import folium

def get_user_ip():
    response = requests.get('https://api.ipify.org')
    return response.text

def get_user_geolocation(ip_address):
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    return response.json()

def display_geolocation_on_map(geolocation):
    try:
        latitude = float(geolocation['lat'])
        longitude = float(geolocation['lon'])
        
        # Check if the coordinates are within the valid range
        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            print("Invalid coordinates")
            return None
        
        map = folium.Map(location=[latitude, longitude], zoom_start=10)
        folium.Marker([latitude, longitude], popup='Your Location').add_to(map)
        return map
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_text_output(geolocation):
    print("Geolocation Information:")
    print(f"IP Address: {geolocation['query']}")
    print(f"City: {geolocation['city']}")
    print(f"Region: {geolocation['region']}")
    print(f"Country: {geolocation['country']}")
    print(f"Latitude: {geolocation['lat']}")
    print(f"Longitude: {geolocation['lon']}")

def main():
    try:
        ip_address = get_user_ip()
        geolocation = get_user_geolocation(ip_address)
        display_text_output(geolocation)
        map = display_geolocation_on_map(geolocation)
        map.save('geolocation_map.html')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()