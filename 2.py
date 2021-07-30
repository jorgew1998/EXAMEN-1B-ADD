#importaciones 
import sys
import couchdb
from tweepy import Stream 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener 
import json

#credenciales
ckey = "iVvt6HXwpRVAn8MuFbPeFq5pI"
csecret = "jEwUHmVViK1Kg53o9a5fKYFcx5IyhpR5oBxKoc5Kh6U4YqSEFT"
atoken = "1415801332238323712-CoN9LkobD6sunH1x9Ccux1QUUsb5HD"
asecret = "21vSseAsN2sxhp4GAIYTSmnMwngrgO24YROJFWliJ06Z3"

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

#conexion couchdb
server = couchdb.Server('http://admin:admin@localhost:5984/')  
try:
    db = server.create('ciudades2')
except:
    db = server('ciudades2')
   
twitterStream.filter(track=['Juegos Olimpicos'])
