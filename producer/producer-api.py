from kafka import KafkaProducer
import json
import time
import requests
# Fonction pour sérialiser les données en JSON
def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# Création du producer Kafka
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=json_serializer
)

# URL de l'API CityBikes
url = "https://api.citybik.es/v2/networks/velib"

while True:
    try:
        # Requête à l'API
        response = requests.get(url)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        data = response.json()

        # Parcours des stations dans la réponse
        stations = data.get('network', {}).get('stations', [])
        for station in stations:
            message = {
                'station_id': station.get('id'),
                'name': station.get('name'),
                'latitude': station.get('latitude'),
                'longitude': station.get('longitude'),
                'free_bikes': station.get('free_bikes'),
                'empty_slots': station.get('empty_slots'),
                'ebikes': station.get('extra', {}).get('ebikes', 0),
                'timestamp': station.get('timestamp')
            }

            # Envoi du message à Kafka
            print(f"Producing message: {message}")
            producer.send('velib_topic', message)

        # Pause avant la prochaine requête
        time.sleep(10)

    except Exception as e:
        print(f"Unexpected error: {e}")
