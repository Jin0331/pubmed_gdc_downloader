from kafka import KafkaProducer
import requests
import json
import time


json_url = "http://openapi.seoul.go.kr:8088/4e4258575a73656d32315a46644370/json/bikeList/1/1000"

# bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
bootstrap_servers = ['210.115.229.96:9091', '210.115.229.96:9092', '210.115.229.96:9093']
topicName = "seoul_bike_1_10"
producer = KafkaProducer(bootstrap_servers = bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


while True:
    try:
        response = requests.get(json_url)
        if response.status_code == 200:
            print("ok! ", end=" ")
            producer.send(topicName, response.json())
            producer.flush()
            time.sleep(10)

    except Exception as e:
        print(e)
        time.sleep(30)          

# # for json
# # value_serializer= lambda v: v.encode('utf-8')
# # producer.send(topicName, msg.encode("utf-8"))
# bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
# topicName = 'test2'
# producer = KafkaProducer(bootstrap_servers = bootstrap_servers,
#                          value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# for index in range(1000):
#     future = producer.send(topicName, {index : "hi"})

# result = future.get(timeout=120)

# producer.flush()
