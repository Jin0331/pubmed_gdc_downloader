# **Kafka-test**

https://medium.com/better-programming/a-simple-apache-kafka-cluster-with-docker-kafdrop-and-python-cf45ab99e2b9

- - -

## **StandAlone**
* **docker-compose 활용**
    1. `SERVERIP=some-value docker-compose up -d ---> back-ground run`

* **kafka-python**
    `pip3 install kafka-python`
    1. **Producer**

        `python3 kafka_producer.py SERVERIP TOPIC_NAME API`

    2. **Consumer**

        `python3 kafka_consumer.py SERVERIP TOPIC_NAME CONSUMER_ID`


 - - -

## **Error reference**

 * https://stackoverflow.com/questions/51799077/kafka-python-consumer-start-reading-from-offset-automatically

* Kafka access inside and outside docker

    1. https://rmoff.net/2018/08/02/kafka-listeners-explained/

    2. https://stackoverflow.com/questions/53247553/kafka-access-inside-and-outside-docker

    3. https://twowinsh87.github.io/etc/2019/09/28/etc-kafka2019-2/