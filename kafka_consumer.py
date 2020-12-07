from kafka import KafkaConsumer
import sys

def consumer_test(SERVERIP, topic_name, GROUPID):

    # bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
    port_list = ["9091", "9092", "9093"]
    bootstrap_servers = [SERVERIP + ":" + port for port in port_list]

    consumer = KafkaConsumer(topic_name, bootstrap_servers= bootstrap_servers,
                            auto_offset_reset='earliest',group_id = GROUPID)

    for message in consumer:
        print (message)

if __name__ == "__main__":
    consumer_test(sys.argv[1], "seoul_bike_1_100", "consumer_test")