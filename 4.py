#importaciones
from facebook_scraper import get_posts
import json
import time
import pymongo
from pymongo import MongoClient

#conexion con mongodb
client =pymongo.MongoClient("mongodb://localhost:27017")
try:
    db=client["Facebook"]
    collection=db["C1"]
except:
    db=client["Facebook"]
    collection=db["C1"]
    
#funcion para guardar en mongodb
 i=1
for post in get_posts("Olympic", pages=50):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
    
    doc['id']=id
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}
        
        doc['post_url']=post['post_url']
        collection.save(doc)
        
        print('guardado con exito')
    except Exception as e:
        print('no se pudo guardar:'+str(e))
