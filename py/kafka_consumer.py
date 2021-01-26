from kafka import KafkaConsumer
import sys

def consumer_test(SERVERIP, topic_name, GROUPID):

    port_list = ["9091", "9092", "9093"]
    bootstrap_servers = [SERVERIP + ":" + port for port in port_list]

    consumer = KafkaConsumer(topic_name, bootstrap_servers= bootstrap_servers,
                            auto_offset_reset='earliest',group_id = GROUPID)

    for message in consumer:
        print (message)

if __name__ == "__main__":

    # python3 kafka_consumer.py SERVERIP TOPIC_NAME CONSUMER_ID
    SERVERIP = sys.argv[1]
    TOPIC_NAME = sys.argv[2]
    CONSUMER_ID = sys.argv[3]

    consumer_test(sys.argv[1], TOPIC_NAME, CONSUMER_ID)