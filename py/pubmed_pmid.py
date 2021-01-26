import urllib.request
import urllib.error
import socket
import json
from http.client import IncompleteRead
from xml.etree import ElementTree as ET
from time import sleep
import lxml
import requests
import os

def getWebData(strUrl, json = dict()):
    code = 404
    delay = 10

    strUrl = strUrl.replace(" ", "%20")

    ## Retry with Error
    while (code != 200):
        try:
            if delay < 200 :
                delay *= 2 
            result = requests.post(strUrl , json=json, timeout=delay)
            code = result.status_code
            
            if code != 200:
                print("{}:{}".format(os.getpid(), str(code)))
                print(strUrl)

        except requests.exceptions.RequestException as e:
            print(e)
            print(code)
            print(strUrl)
            
        else:
            if result.text.encode('utf-8') == None:
                print("None Error")
                code = 404
                

    return result.text.encode('utf-8')

def getPmidList(strQuery):
    retmax = 1000000000 # as possible as max;
    strUrl = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={0}&retmax={1}&retmode=json'.format(strQuery, retmax)

    ## Get HTML Data
    pmidList = getWebData(strUrl)
    
    pmidList = json.loads(pmidList)

    pmidList = list(map(int, pmidList['esearchresult']['idlist']))

    return pmidList