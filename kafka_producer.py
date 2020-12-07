from kafka import KafkaProducer
import json

bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
topicName = 'test2'

# for json
# value_serializer= lambda v: v.encode('utf-8')
# producer.send(topicName, msg.encode("utf-8"))
producer = KafkaProducer(bootstrap_servers = bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for index in range(1000):
    future = producer.send(topicName, {index : "hi"})

result = future.get(timeout=120)

producer.flush()
