from kafka import KafkaProducer
import json
import time
import requests
from bs4 import BeautifulSoup

def json_serializer(data):
    """
    Sérialise les données Python en format JSON pour l'envoi via Kafka.
    """
    return json.dumps(data).encode('utf-8')

# Création du producteur qui pointe vers notre cluster Kafka (localhost:9092)
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092,kafka:9093'],
    value_serializer=json_serializer
)

while True:
    """
    Boucle infinie pour récupérer et envoyer les données en continu.
    """
    url = "https://api.citybik.es/v2/networks/velib"

    try:
        """
        Envoie une requête GET à l'API Velib et récupère les données.
        """
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
       
        station_data = json.loads(response.text)  # Parse la réponse JSON

        # Extraction des données pertinentes de la station
        station_id = station_data['station_id']
        station_name = station_data['station_name']
        free_bikes = station_data['free_bikes']
        empty_slots = station_data['empty_slots']
        timestamp = station_data['timestamp']

        message = {
            'station_id': station_id,
            'station_name': station_name,
            'free_bikes': free_bikes,
            'empty_slots': empty_slots,
            'timestamp': timestamp
        }

        print(f"Envoi du message : {message}")
        producer.send('velib_topic', message)  # Envoie le message au topic spécifié
        producer.flush()  # Force l'envoi immédiat du message
        time.sleep(2)  # Pause de 2 secondes avant la prochaine requête

    except Exception as e:
        """
        Gestion des erreurs potentielles.
        """
        print(f"Erreur inattendue : {e}")