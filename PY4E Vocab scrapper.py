from bs4 import BeautifulSoup
import pandas
import time
import requests

#Get website data
def get_glossary_data(url):
    response = requests.get(url)
    
