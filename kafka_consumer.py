from kafka import KafkaConsumer
# group_id 
bootstrap_servers = ['210.115.229.96:9091', '210.115.229.96:9092', '210.115.229.96:9093']
# bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
consumer = KafkaConsumer("seoul_bike_1_10", bootstrap_servers= bootstrap_servers,
                          auto_offset_reset='earliest',group_id='consumer2')

for message in consumer:
    print (message)