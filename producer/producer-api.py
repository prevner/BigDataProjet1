from kafka import KafkaProducer
import json
import time
import requests

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# Création du producer Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=json_serializer
)

while True:
    url = "https://api.citybik.es/v2/networks/velib"
    try:
        # Requête API pour récupérer les données des stations Vélib
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Récupération des stations
        stations = data.get("network", {}).get("stations", [])
        
        # Parcours des stations et envoi des données pertinentes à Kafka
        for station in stations:
            message = {
                "station_name": station.get("name"),
                "free_bikes": station.get("free_bikes"),
                "ebikes": station.get("extra", {}).get("ebikes"),
                "empty_slots": station.get("empty_slots"),
                "total_slots": station.get("extra", {}).get("slots"),
                "latitude": station.get("latitude"),
                "longitude": station.get("longitude"),
                "timestamp": time.time()
            }
            print(f"Producing message: {message}")
            producer.send('velib_topic', message)  # Envoi au topic Kafka
            producer.flush()  # Confirme l'envoi

        # Pause avant la prochaine requête
        time.sleep(10)  # Met à jour toutes les 10 secondes
        
    except Exception as e:
        print(f"Unexpected error: {e}")
