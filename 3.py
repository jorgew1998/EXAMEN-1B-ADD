#importaciones y conexion a mongodb
from pymongo import MongoClient
myClient = MongoClient ('mongodb://localhost:27017/')
try:
    myClient.admin.command('ismaster')
    print('MongoDB connection: Succes')
except ConnectionFailure as cf:
    print('MongoDB connection: Succes', cf)
    
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
import json
from bson.raw_bson import RawBSONDocument

def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))
 
response = requests.get('https://olympics.com/tokyo-2020/es/')
soup = BeautifulSoup(response.content, "lxml")

Titles=[]

#se escoge la etiqueta span
post_titles= soup.find_all("span", class_="tk-card__titlelink")

#for para limpiar
for element in post_titles:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Titles.append(limpio.strip())


print(Titles)

#se guarda en dataframe con pandas y se lo envia a mongodb
archivo = pd.DataFrame(Titles, index=Titles)
archivo.to_json('datos.json')

db = myClient["JuegosO"]
Collection= db["noticias"]

with open('datos.json') as file:
    file_data = json.load(file)

    
if isinstance (file_data, list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)
