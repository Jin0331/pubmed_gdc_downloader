from Bio import Entrez
import pandas as pd
import requests
import json
import urllib.request
import urllib.error
from http.client import IncompleteReady
from xml.etree import ElementTree as ET
import lxml
import os


# Pubmed pmid extraction
#https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.ESearch
def pmid_search(query, retstart):
    Entrez.email = 'sempre813@kakao.com'
    handle = Entrez.esearch(db = "pubmed",
                            retstart = retstart,
                            sort= "relevance",
                            retmax = 100000,
                            retmod = "xml",
                            mindate = "2017/01/01",
                            maxdate = "2021/02/01",
                            term = query)
    results = Entrez.read(handle)
    return results

if __name__ == "__main__":
    
    os.chdir('/home/jovyan/work/Pubmed-Batch-Download')
    
    # "cancer" AND "immune checkpoint" AND "new target"
    # "cancer" AND "immune checkpoint" AND "first-in-class"
    # "cancer" AND "immune checkpoint" AND "first-in-class"
    # "cancer" AND "first-in-class"

    query = '"cancer" AND "immune checkpoint" AND "first-in-class"'
    data = pmid_search(query = query, retstart=0)
    df = pd.DataFrame(data['IdList'])
    print(df.count())
    df.to_csv("pmid_data/temp.csv", sep = "\n", index = False, header = None)

    # pmid deliver 
    start_ = input("Download PDF :")
    if start_ == "yes" or start_ == "y":
        os.system("python /home/jovyan/work/Pubmed-Batch-Download/fetch_pdfs.py -pmf /home/jovyan/work/Pubmed-Batch-Download/pmid_data/temp.csv")
