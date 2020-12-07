from kafka import KafkaProducer

bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
topicName = 'my-topic-three'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

msg = "hellow world, kafka2!"

producer.send(topicName, msg.encode("utf-8"))
producer.flush()
