from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer
import requests
import json
import time
import sys

def create_topic(SERVER, TOPIC_name):
    # port number in docker-compose.yml
    port_list = ["9091", "9092", "9093"]
    bootstrap_servers = [SERVERIP + ":" + port for port in port_list]
    admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers, 
                                    client_id='test')
    topic_list = []
    # partition number, replica number checking!!
    topic_list.append(NewTopic(name=TOPIC_name, num_partitions=3, replication_factor=3))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)

def send_mag(url, SERVERIP, TOPIC_name):
    port_list = ["9091", "9092", "9093"]
    bootstrap_servers = [SERVERIP + ":" + port for port in port_list]
    topicName = TOPIC_name
    producer = KafkaProducer(bootstrap_servers = bootstrap_servers,
                            value_serializer=lambda v: json.dumps(v).encode('euc-kr'))
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # msg send to broker
                producer.send(topicName, response.json())
                producer.flush()

                # console print        
                sys.stdout.write("ok!!! ")  # same as print
                sys.stdout.flush()
                
                time.sleep(30)

        except Exception as e:
            print(e)
            time.sleep(30)


if __name__ == "__main__":
    
    # python3 kafka_producer.py SERVERIP TOPIC_NAME API
    SERVERIP = sys.argv[1]
    TOPICNAME = sys.argv[2]
    API = sys.argv[3]

    # create topic
    create_topic(SERVERIP, TOPICNAME)

    # send message
    send_mag(API, SERVERIP, TOPICNAME)