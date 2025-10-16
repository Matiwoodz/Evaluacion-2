import requests
import urllib.parse


route_url = "https://graphhopper.com/api/1/route?"

key = "4e0d94dc-ded1-4012-a702-b69f88428e03"


def geocoding(location, key):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": key})
    
    try:
        replydata = requests.get(url)
        json_data = replydata.json()
        json_status = replydata.status_code

        if json_status == 200 and len(json_data.get("hits", [])) != 0:
            hit = json_data["hits"][0]
            lat = hit.get("point", {}).get("lat")
            lng = hit.get("point", {}).get("lng")
            name = hit.get("name", "")
            value = hit.get("osm_value", "")
            country = hit.get("country", "")
            state = hit.get("state", "")

            if state and country:
                new_loc = f"{name}, {state}, {country}"
            elif country:
                new_loc = f"{name}, {country}"
            else:
                new_loc = name

            print(f"URL de la API de Geocodificación para {new_loc} (Tipo: {value})\n{url}")
            return json_status, lat, lng, new_loc
        else:
            lat = "null"
            lng = "null"
            new_loc = location
            if json_status != 200 and "message" in json_data:
                print(f"Estado de la API de Geocodificación: {json_status}\nMensaje de error: {json_data['message']}")
            return json_status, lat, lng, new_loc

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None, "null", "null", location



while True:
    print("\n+++++++++++++++++++++++++++++++++++++++++++++")
    print("Perfiles de vehículo disponibles en Graphhopper:")
    print("+++++++++++++++++++++++++++++++++++++++++++++")

    print("auto, bicicleta, a pie")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    

    perfiles_vehiculo = {
        "auto": "car",
        "bicicleta": "bike",
        "a pie": "foot"
    }
    
    vehiculo_es = input("Ingrese un perfil de vehículo de la lista de arriba (o 's' para salir): ").lower()
    
    if vehiculo_es in ["salir", "s"]:
        break
    

    if vehiculo_es not in perfiles_vehiculo:
        print("No se ingresó un perfil de vehículo válido. Usando 'auto'.")
        vehiculo_es = "auto"
    

    vehicle_api = perfiles_vehiculo[vehiculo_es]

    loc1 = input("Lugar de Origen: ")
    if loc1.lower() in ["salir", "s"]:
        break
    orig = geocoding(loc1, key)

    loc2 = input("Destino: ")
    if loc2.lower() in ["salir", "s"]:
        break
    dest = geocoding(loc2, key)
    
    print("=====================================================")
    
    if orig and dest and orig[0] == 200 and dest[0] == 200:
        op = f"&point={orig[1]}%2C{orig[2]}"
        dp = f"&point={dest[1]}%2C{dest[2]}"
        
        paths_url = route_url + urllib.parse.urlencode({"key": key, "vehicle": vehicle_api, "locale": "es"}) + op + dp
        
        try:
            paths_response = requests.get(paths_url)
            paths_status = paths_response.status_code
            paths_data = paths_response.json()
            
            print(f"Estado de la API de Rutas: {paths_status}")
            print(f"URL de la API de Rutas:\n{paths_url}")
            
            print("=====================================================")
     
            print(f"Direcciones desde {orig[3]} hasta {dest[3]} en {vehiculo_es}")
            print("=====================================================")
            
            if paths_status == 200 and "paths" in paths_data:
                path_info = paths_data["paths"][0]
                km = path_info["distance"] / 1000
                sec = int(path_info["time"] / 1000 % 60)
                min = int(path_info["time"] / 1000 / 60 % 60)
                hr = int(path_info["time"] / 1000 / 60 / 60)
                
      
                print("Distancia del Viaje: {0:.2f} km".format(km))
                print("Duración del Viaje: {0:02d}:{1:02d}:{2:02d}".format(hr, min, sec))
                print("=====================================================")

                for instruction in path_info["instructions"]:
                    path_text = instruction["text"]
                    distancia_km = instruction["distance"] / 1000
                    
                    path_text = path_text.replace("and drive toward", "y conduce hacia")
                    path_text = path_text.replace("toward", "hacia")
                    path_text = path_text.replace("Arrive at destination", "¡Fin del recorrido!")

               
                    print("{0} ({1:.2f} km)".format(path_text, distancia_km))
                print("=====================================================")
            else:
                error_message = paths_data.get("message", "Ruta no encontrada.")
                print(f"Mensaje de Error: {error_message}")
                print("*************************************************")
        
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión al solicitar la ruta: {e}")
