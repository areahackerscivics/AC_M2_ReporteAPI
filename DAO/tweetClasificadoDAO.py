#!/usr/bin/env python
# encoding: utf-8
import sys, os
import numpy as np
parent_dir=os.getcwd()
path= os.path.dirname(parent_dir)
sys.path.append(path)

from pymongo import MongoClient
from DAO.conexionMongo import *

from datetime import datetime
import dateutil.parser

def getTweetsClasificados(anyo, mes):

    conexion = getConexion()
    client = MongoClient(conexion)
    tdb = getDB()
    db = client[tdb]
    coleccion = getCollTweetsClas()
    tweetsClasificados = db[coleccion]

    ini = anyo + '-' + mes + '-01 00:00:00'
    ini=datetime.strptime(ini,"%Y-%m-%d %H:%M:%S")

    fin = anyo + '-' + mes + '-31 23:59:59'
    fin=datetime.strptime(fin,"%Y-%m-%d %H:%M:%S")

    tw = tweetsClasificados.find({
                                        'fechaTweet':{
                                            '$gte': ini,
                                            '$lt':  fin
                                        }
                                    })

    return list(tw)
