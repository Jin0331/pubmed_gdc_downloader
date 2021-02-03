from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer

from Bio import Entrez
import requests
import json
import time
import sys
import urllib.request
import urllib.error
import socket
from http.client import IncompleteRead
from xml.etree import ElementTree as ET
import lxml
import os


# Pubmed pmid extraction
def pmid_search(query, retstart):
    Entrez.email = 'sempre813@kakao.com'
    handle = Entrez.esearch(db = "pubmed",
                            retstart = retstart,
                            sort= "relevance",
                            retmax = 100000,
                            retmod e = "xml",
                            term = query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'your.email@example.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results

# Kafka producer
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
    return

def send_mag(SERVERIP, TOPIC_name, query, retstart):
    port_list = ["9091", "9092", "9093"]
    bootstrap_servers = [SERVERIP + ":" + port for port in port_list]
    topicName = TOPIC_name
    producer = KafkaProducer(bootstrap_servers = bootstrap_servers,
                            value_serializer = lambda v: json.dumps(v).encode('utf-8'))
    while True:
        try:
            # msg send to broker
            data = pmid_search(query=query, retstart=retstart)
            print("first : " , data["IdList"][0], " last : ", data["IdList"][-1])

            producer.send(topicName, data["IdList"])
            producer.flush()

            # console print        
            now = time.localtime()
            sys.stdout.write("%04d/%02d/%02d done! \n" % (now.tm_year, now.tm_mon, now.tm_mday))  # 현재시간 출력
            sys.stdout.flush()
                
            time.sleep(300)
            retstart += 100001 # changes offset for pmid
        except Exception as e:
            print(e)
            time.sleep(300)


if __name__ == "__main__":
    
    # python3 kafka_producer.py SERVERIP TOPIC_NAME API
    SERVERIP = sys.argv[1]
    TOPICNAME = sys.argv[2]
    pubmed_keyword = sys.argv[3]

    # create topic
    try :
        create_topic(SERVERIP, TOPICNAME)
    except Exception as e:
        print(e)

    # send message
    send_mag(SERVERIP = SERVERIP, 
             TOPIC_name = TOPICNAME, 
             query = pubmed_keyword,
             retstart= 0)