#!/usr/bin/env python
# encoding: utf-8

import sys, os
import datetime
parent_dir=os.getcwd()
path= os.path.dirname(parent_dir)
sys.path.append(path)


from pymongo import MongoClient
from DAO.conexionMongo import *

conexion = getConexion()
client = MongoClient(conexion)
tdb = getDB()
db = client[tdb]
coleccion = getCatalogo()
dbCatalogo = db[coleccion]




def getCatalogoBLL(anyo, mes):

   try:
       datosM = dbCatalogo.find_one({
                                           "anyo": anyo,
                                           "mes": mes
                                           })
   except Exception as e:
       print "     ", "- Error en find catalogo: ", type(e), e

   respuesta = []
   datos = datosM["datos"]
   for dato in datos:
       dicDato = {}
       print dato

       dicDato["Categoría"] = str(dato["categoria"].encode('UTF-8'))
       dicDato["Nº Datasets"] = dato["numDatasets"]


       respuesta.append(dicDato)
   return respuesta
