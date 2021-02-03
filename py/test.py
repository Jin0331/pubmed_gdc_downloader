from Bio import Entrez

def search(query, retstart, retmax):
    Entrez.email = 'your.email@example.com'
    handle = Entrez.esearch(db = "pubmed",
                            retstart = retstart,
                            sort= "relevance",
                            retmax = retmax,
                            retmode = "xml",
                            term = query)
    results = Entrez.read(handle)
    return results


#result = search(query="PRKN", retstart=1, retmax=10000000)
#print(result)


from kafka import KafkaProducer
import logging
import json
logging.basicConfig(level=logging.INFO)

port_list = ["9091", "9092", "9093"]
bootstrap_servers = ["210.115.229.80" + ":" + port for port in port_list]
topicName = "test8"
producer = KafkaProducer(bootstrap_servers = bootstrap_servers,
                            value_serializer = lambda v: json.dumps(v).encode('utf-8'))
producer.send(topicName, ["123"])
producer.send(topicName, ["456"])

result = search(query="PRKN", retstart=10000000, retmax=10000000)
producer.send(topicName, result["IdList"])

producer.flush()

