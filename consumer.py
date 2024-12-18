from kafka import KafkaConsumer
import json

def json_deserializer(data):
    return json.loads(data.decode('utf-8'))

consumer = KafkaConsumer(
    'test_topic',
    bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094'],
    value_deserializer=json_deserializer,
    auto_offset_reset='earliest'
)

for message in  consumer:
    print(f"Message reçu: {message.value}")