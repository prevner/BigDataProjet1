from kafka import KafkaProducer
import json
import time
import requests

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# Vérifiez l'adresse et le port du serveur Kafka
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],  # Assurez-vous que cette adresse est correcte
    value_serializer=json_serializer
)

while True:
    url = "https://api.citybik.es/v2/networks/velib"
    try:
        response = requests.get(url)
        data = response.json()

        # Extraction des stations et leurs informations
        stations = data['network']['stations']
        for station in stations:
            station_info = {
                'station_id': station['id'],
                'station_name': station['name'],
                'latitude': station['latitude'],
                'longitude': station['longitude'],
                'free_bikes': station['free_bikes'],
                'empty_slots': station['empty_slots'],
                'extra': station['extra'],  # Récupération des informations supplémentaires
                'timestamp': station['timestamp']
            }
            print(f"Producing message: {station_info}")
            producer.send('velib_topic', station_info)  # Utilise le producer pour envoyer un objet
            producer.flush()  # Demande au producer d'attendre que le message soit bien envoyé
        
        time.sleep(60)  # Pause d'une minute entre les appels à l'API
        
    except Exception as e:
        print(f"Unexpected error: {e}")
