# **Pubmed paper(PDF) to MongoDB**

## **docker-compose.yml**

* **docker-compose 활용**

    1. `SERVERIP=your-ip docker-compose up -d`

    2. `Zookeeper 3.4.9, Kafka cp-kafka:5.3.0, 3 server`

<br>

 - - -

<br>

## **MongoDB**

    MongoDB 4.4.3 Mongo-Express

    user: root, passwd: USER_PASSWORD

## **All-spark-notebook**

    Spark 3.0.1, Python 3.8.3, R 4.0.3, Jupyter Lab, VScode

    apt-get update && apt-get upgrade

1. **passwd**

    `passwd`

    `passwd jovyan`

2. **openssh-server**

    ``apt-get install openssh-server ufw``

    ``echo "PermitRootLogin yes" >> /etc/ssh/sshd_config``

    ``service ssh start``

3. **vccode**

    `Python interpreter install & Python Extension pack(debug console)`

3. **Python modules**

    ``pip3 install --upgrade pip``

    A. **kafka-python**

        pip3 install kafka-python

        1. Producer

            python3 kafka_producer.py SERVERIP TOPIC_NAME API

        2. Consumer

            python3 kafka_consumer.py SERVERIP TOPIC_NAME CONSUMER_ID

    B. **pymongo**

        pip3 install "pymongo==3.11.2"  gridfs automatically install

<br>

- - -

<br>

## **Error reference**

* https://medium.com/better-programming/a-simple-apache-kafka-cluster-with-docker-kafdrop-and-python-cf45ab99e2b9

 * https://stackoverflow.com/questions/51799077/kafka-python-consumer-start-reading-from-offset-automatically

* Kafka access inside and outside docker

    1. https://rmoff.net/2018/08/02/kafka-listeners-explained/

    2. https://stackoverflow.com/questions/53247553/kafka-access-inside-and-outside-docker

    3. https://twowinsh87.github.io/etc/2019/09/28/etc-kafka2019-2/

* Store a PDF file in my MongoDB database with PYmongo error

    1. https://stackoverflow.com/questions/58165966/store-a-pdf-file-in-my-mongodb-database-with-pymongo-error