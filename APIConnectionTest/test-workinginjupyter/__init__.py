import mysql.connector
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

conn = mysql.connector.connect(user="EnxiJessieMarian",
                               passwd="SoftwareEngineering2019",
                               host="dublinbikesdata.cmgmbuuwvwd0.eu-west-1.rds.amazonaws.com",
                               database='DublinBikesData')

data = requests.get("https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=166048e0e00bbc76dd9a53d07bab98427b29d1e0")
#status_code = 200
data.content.decode("utf-8")