from kafka import KafkaConsumer
# consumer.subscribe(['test2'])
# group_id 
consumer = KafkaConsumer("seoul_bike_1_10", bootstrap_servers=['localhost:9091','localhost:9092','localhost:9093'],
                          auto_offset_reset='earliest',group_id='consumer')

for message in consumer:
    print (message)