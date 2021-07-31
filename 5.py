#importaciones
from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument
from pymongo.errors import ConnectionFailure
import sqlite3

#conecxion con la BD creada
base = sqlite3.connect("BD1.db")

#Lectura de archivos csv obtendios de tiktok
df0 = pd.read_csv('C:/Users/EQUIPO/Desktop/prueba/brasilnasolimpiadas_1627693662496.csv', index_col=0)
df1 = pd.read_csv('C:/Users/EQUIPO/Desktop/prueba/olimpiadasdetokio_ofc_1627693630814.csv', index_col=0)

#Traslado de datos csv a sqlite
df0.to_sql('olimpiadas', base)
df1.to_sql('olimpiadas1', base)
