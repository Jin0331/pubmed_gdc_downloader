# **pubmed_gdc_downloader**

## **docker-compose.yml**

* **docker-compose 활용**

    1. `SERVERIP=[server-ip] PASSWORD=[password] docker-compose up -d`

    2. `Zookeeper 3.4.9, Kafka cp-kafka:5.3.0, 3 server`

<br>

 - - -

<br>

## **MongoDB**

    MongoDB 4.4.3 Mongo-Express

    user: root, passwd: USER_PASSWORD

## **All-spark-notebook**

    Spark 3.0.1, Python 3.8.3, R 4.0.3, Jupyter Lab, VScode

    apt-get update && apt-get upgrade -y

    conda update -y conda

1. **passwd**

    `passwd`

    `passwd jovyan`

2. **openssh-server**

    ``apt-get install openssh-server iputils-ping -y``

    ``echo "PermitRootLogin yes" >> /etc/ssh/sshd_config``

    ``service ssh start``

3. **vccode**

    `Pulgin:Python Extension Pack`

4. **Python** - ***conda env base***

    ``pip3 install --upgrade pip``

    A. **kafka-python**

        pip3 install kafka-python

        1. Producer

            python3 kafka_producer.py SERVERIP TOPIC_NAME API

        2. Consumer

            python3 kafka_consumer.py SERVERIP TOPIC_NAME CONSUMER_ID

    B. **pymongo**

        pip3 install "pymongo==3.11.2" (gridfs automatically install)
    
    C. **biopython**

        pip3 install biopython

    D. **Pubmed-Bach-Download**

        pip3 install requests requests3 beautifulsoup4 lxml

        git clone https://github.com/Jin0331/Pubmed-Batch-Download.git

        usage: fetch_pdfs.py [-h] [-pmids PMIDS] [-pmf PMF] [-out OUT] [-errors ERRORS] [-maxRetries MAXRETRIES]

        Flag Arguments:
        -h, --help            show this help message and exit
        -pmids PMIDS          Comma separated list of pmids to fetch. Must include -pmids or -pmf.
        -pmf PMF              File with pmids to fetch inside, one pmid per line. Optionally, the file can be a tsv with a second column of names to save each pmid's article with (without '.pdf' at the end). Must include -pmids or -pmf
        -out OUT              Output directory for fetched articles. Default: fetched_pdfs
        -errors ERRORS        Output file path for pmids which failed to fetch. Default: unfetched_pmids.tsv
        -maxRetries MAXRETRIES
                                Change max number of retries per article on an error 104. Default: 3
    E. **airflow**

        1. conda install -y airflow

        2. airflow initdb

        3. 
            echo 'export AIRFLOW_HOME=~/airflow' >> /root/.profile
            echo 'export AIRFLOW_HOME=~/airflow' >> /root/.bashrc
            source /root/.profile

5. **Python** - ***conda env gdc_client***

    ``conda create -n gdc_client python=3.7``

    ``conda activate gdc_client``

    ``git clone https://github.com/NCI-GDC/gdc-client.git``

        pip install -r requirements.txt
        python setup.py install
        pip install -r dev-requirements.txt

        python -m pytest tests/


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

* biopython - entrez

    1. https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.ESearch
    
    2. https://marcobonzanini.com/2015/01/12/searching-pubmed-with-python/

* postgre

    1. https://github.com/khezen/compose-postgres

* airflow

    1. https://blog.naver.com/wideeyed/221565240108# Mongodb
