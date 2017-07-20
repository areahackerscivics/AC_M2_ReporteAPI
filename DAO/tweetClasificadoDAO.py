#!/usr/bin/env python
# encoding: utf-8
import sys, os
import calendar
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


    anyoA = int(anyo)
    mesA = int(mes)

    diasMes = int( calendar.monthrange(anyoA, mesA)[1] )


    ini = anyo + '-' + mes + '-01 00:00:00'
    ini=datetime.strptime(ini,"%Y-%m-%d %H:%M:%S")

    fin = anyo + '-' + mes + '-'+ str(diasMes) + ' 23:59:59'
    fin=datetime.strptime(fin,"%Y-%m-%d %H:%M:%S")

    tw = tweetsClasificados.find({
                                        'fechaTweet':{
                                            '$gte': ini,
                                            '$lt':  fin
                                        }
                                    })

    return list(tw)

def getTweetsClasificadosdias(anyo, mes):

    conexion = getConexion()
    client = MongoClient(conexion)
    tdb = getDB()
    db = client[tdb]
    coleccion = getCollTweetsClas()
    tweetsClasificados = db[coleccion]

    anyo1=int(anyo)
    mes1=int(mes)
    diasMes=int(calendar.monthrange(anyo1, mes1)[1])

    ini = anyo + '-' + mes + '-01 00:00:00'
    ini=datetime.strptime(ini,"%Y-%m-%d %H:%M:%S")

    fin = anyo + '-' + mes + '-'+str(diasMes)+' 23:59:59'
    fin=datetime.strptime(fin,"%Y-%m-%d %H:%M:%S")
    pipeline=[
    { "$match": {'fechaTweet':{'$gte': ini, '$lte':  fin}}},
    {"$project": {"_id":0,"categoria":1,
                            "fechaTweet": { "$dateToString": { "format": "%d", "date": "$fechaTweet" } } }},
              {"$group":{"_id":{"categoria":"$categoria","fechaTweet":"$fechaTweet"},"total":{"$sum":1}}},
              {"$project": {"_id":0,"categoria":"$_id.categoria","dia":"$_id.fechaTweet", "total":"$total"}},
              {"$sort":{"dia":1}}]
    tw=tweetsClasificados.aggregate(pipeline)
    return list(tw)
