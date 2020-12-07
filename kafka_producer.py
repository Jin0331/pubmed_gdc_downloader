from kafka import KafkaProducer
import requests
import json
import time
import sys

def topic_producer(url, SERVERIP, topic_name):
    # bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
    port_list = ["9091", "9092", "9093"]
    bootstrap_servers = [SERVERIP + ":" + port for port in port_list]
    topicName = topic_name
    producer = KafkaProducer(bootstrap_servers = bootstrap_servers,
                            value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    while True:
        try:
            response = requests.get(json_url)
            if response.status_code == 200:
                producer.send(topicName, response.json())
                producer.flush()
                print("ok! ", end=" ")
                time.sleep(60)

        except Exception as e:
            print(e)
            time.sleep(30)

if __name__ == "__main__":
    json_url = "http://openapi.seoul.go.kr:8088/4e4258575a73656d32315a46644370/json/bikeList/1/100"
    topic_producer(json_url, sys.argv[1], "seoul_bike_1_100")