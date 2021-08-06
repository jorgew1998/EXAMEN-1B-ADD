#importaciones 
import sys
import couchdb
from tweepy import Stream 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener 
import json

#credenciales
ckey = *************************
csecret = *************************
atoken = *****************************
asecret = ******************************


class listener(StreamListener):
    
    def on_data(self, data):
        archiTweet = json.loads(data)
        try:
            
            archiTweet["_id"] = str(archiTweet['id'])
            doc = db.save(archiTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

#conexion con couchdb
server = couchdb.Server('http://admin:admin@localhost:5984/')  
try:
    db = server.create('cuidades')
except:
    db = server('ciudades')

#Localizaciones de Tokio, Moscu y Atlanta    
#Tokyo
twitterStream.filter(locations=[-78.619545,-0.365889,-78.441315,-0.047208])
#Moscu
#twitterStream.filter(locations=[-70.7250339,7.1068005,-70.7250339,7.1068005])
#Atlanta
#twitterStream.filter(locations=[-84.55106806,33.64780797,-84.28956005,33.88682297])
