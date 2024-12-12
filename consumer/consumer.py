from kafka import KafkaConsumer
import json
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def json_deserializer(data):
    return json.loads(data.decode('utf-8'))

# Initialisation du KafkaConsumer
consumer = KafkaConsumer(
    'velib_topic',  # Assurez-vous que le topic correspond à celui utilisé par le producer
    bootstrap_servers=['kafka:9092','kafka2:9093'],
    value_deserializer=json_deserializer,
    auto_offset_reset='earliest',  # Lire depuis le début si aucun offset n'est présent
    enable_auto_commit=False,  # Sauvegarde automatique des offsets
    group_id='velib_consumer_group'  # Permet de gérer les consommateurs en groupe
)

logging.info("Kafka Consumer démarré et en attente de messages...")

# Traitement des messages
try:
    for message in consumer:
        try:
            data = message.value
            logging.info(f"Message reçu: {data}")

            # Analyse ou traitement du message
            station_id = data.get('station_id')
            station_name = data.get('station_name')
            free_bikes = data.get('free_bikes')
            empty_slots = data.get('empty_slots')
            extra = data.get('extra')
            timestamp = data.get('timestamp')

            # Exemple de traitement : affichage des données pertinentes
            logging.info(f"Station: {station_name} (ID: {station_id}) | Free Bikes: {free_bikes},Extra: station{extra}, Empty Slots: {empty_slots}, Timestamp: {timestamp}")

        except Exception as process_err:
            logging.error(f"Erreur lors du traitement du message: {process_err}")

except KeyboardInterrupt:
    logging.info("Arrêt manuel du consommateur.")
except Exception as e:
    logging.error(f"Erreur inattendue: {e}")
finally:
    logging.info("Kafka Consumer arrêté.")
