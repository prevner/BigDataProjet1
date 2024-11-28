from kafka import KafkaConsumer
import json
import time 

def json_serializer(data):
    return json.dumps(data).encode('utf-8')