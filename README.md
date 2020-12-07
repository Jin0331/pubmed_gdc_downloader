# Kafka-test

https://medium.com/better-programming/a-simple-apache-kafka-cluster-with-docker-kafdrop-and-python-cf45ab99e2b9

- - -

## 단일 서버
* **docker-compose 활용**
* **1. pip3 install kafka-python**
* **2. SERVERIP=some-value docker-compose up -d ---> back-ground run**

* **3. kafka_producer.py SERVERIP**
* **4. kafka_consumer.py SERVERIP**
 - - -
 https://stackoverflow.com/questions/51799077/kafka-python-consumer-start-reading-from-offset-automatically

* Kafka access inside and outside docker
 https://rmoff.net/2018/08/02/kafka-listeners-explained/

 https://stackoverflow.com/questions/53247553/kafka-access-inside-and-outside-docker

 https://twowinsh87.github.io/etc/2019/09/28/etc-kafka2019-2/