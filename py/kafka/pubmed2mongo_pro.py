from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer
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
def getWebData(strUrl, json = dict()):
    code = 404
    delay = 10

    strUrl = strUrl.replace(" ", "%20")

    ## Retry with Error
    while (code != 200):
        try:
            if delay < 200 :
                delay *= 2 
            result = requests.post(strUrl , json=json, timeout=delay)
            code = result.status_code
            
            if code != 200:
                print("{}:{}".format(os.getpid(), str(code)))
                print(strUrl)

        except requests.exceptions.RequestException as e:
            print(e)
            print(code)
            print(strUrl)
            
        else:
            if result.text.encode('utf-8') == None:
                print("None Error")
                code = 404
                

    return result.text.encode('utf-8')

def getPmidList(strQuery):
    retmax = 1000000000 # as possible as max;
    strUrl = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={0}&retmax={1}&retmode=json'.format(strQuery, retmax)

    ## Get HTML Data
    pmidList = getWebData(strUrl)    
    pmidList = json.loads(pmidList)
    pmidList = list(map(int, pmidList['esearchresult']['idlist']))

    return pmidList


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

def send_mag(SERVERIP, TOPIC_name, pubmed_keyword):
    port_list = ["9091", "9092", "9093"]
    bootstrap_servers = [SERVERIP + ":" + port for port in port_list]
    topicName = TOPIC_name
    producer = KafkaProducer(bootstrap_servers = bootstrap_servers,
                            value_serializer = lambda v: json.dumps(v).encode('utf-8'))
    while True:
        try:
            # msg send to broker
            data = getPmidList(pubmed_keyword)
            producer.send(topicName, getPmidList(data))
            producer.flush()

            # console print        
            now = time.localtime()
            sys.stdout.write("%04d/%02d/%02d done! \n" % (now.tm_year, now.tm_mon, now.tm_mday))  # 현재시간 출력
            sys.stdout.flush()
                
            time.sleep(60)

        except Exception as e:
            print(e)
            time.sleep(30)


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
    send_mag(SERVERIP = SERVERIP, TOPIC_name = TOPICNAME, pubmed_keyword = pubmed_keyword)