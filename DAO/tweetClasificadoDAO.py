#!/usr/bin/env python
# encoding: utf-8
import sys, os
import calendar
parent_dir=os.getcwd()
path= os.path.dirname(parent_dir)
sys.path.append(path)

from pymongo import MongoClient
from DAO.conexionMongo import *

from datetime import datetime


def getTweetsClasificados(anyo, mes):
    """Consulta los tweets clasificados.

    Devuelve en una lista los tweets creados en
    determinado año y mes y que han sido clasificados.
    Para ello hace la consulta a la Base de datos.

    Parámetros:
    anyo: Año en el que fue creado el Tweet
    mes: Mes en el que fue creado el Tweet

    """

    conexion = getConexion()
    client = MongoClient(conexion)
    tdb = getDB()
    db = client[tdb]
    coleccion = getCollTweetsClas()
    tweetsClasificados = db[coleccion]

    #Se búsca el último día del mes usando la función calendario
    anyoA = int(anyo)
    mesA = int(mes)
    diasMes = int( calendar.monthrange(anyoA, mesA)[1] )

    #Se cambia el formato de la fecha para que tome desde la
    #primera hora del dias hasta la ultima hora del último día
    ini = anyo + '-' + mes + '-01 00:00:00'
    ini=datetime.strptime(ini,"%Y-%m-%d %H:%M:%S")

    fin = anyo + '-' + mes + '-'+ str(diasMes) + ' 23:59:59'
    fin=datetime.strptime(fin,"%Y-%m-%d %H:%M:%S")
    #------------------------------------------------------

    tw = tweetsClasificados.find({
                                        'fechaTweet':{
                                            '$gte': ini,
                                            '$lt':  fin
                                        }
                                    })

    return list(tw)

def getTweetsClasificadosdias(anyo, mes):
    """Consulta los tweets clasificados diariamente.

    Devuelve en una lista (categoría,dia, total) los tweets creados
    en un determinado año y mes y que han sido clasificados.
    Para ello hace la consulta a la Base de datos.

    Parámetros:
    anyo: Año en el que fue creado el Tweet
    mes: Mes en el que fue creado el Tweet

    """
    conexion = getConexion()
    client = MongoClient(conexion)
    tdb = getDB()
    db = client[tdb]
    coleccion = getCollTweetsClas()
    tweetsClasificados = db[coleccion]

    #Se búsca el último día del mes usando la función calendario
    anyo1=int(anyo)
    mes1=int(mes)
    diasMes=int(calendar.monthrange(anyo1, mes1)[1])

    #Se cambia el formato de la fecha para que tome desde la
    #primera hora del dias hasta la ultima hora del último día

    ini = anyo + '-' + mes + '-01 00:00:00'
    ini=datetime.strptime(ini,"%Y-%m-%d %H:%M:%S")

    fin = anyo + '-' + mes + '-'+str(diasMes)+' 23:59:59'
    fin=datetime.strptime(fin,"%Y-%m-%d %H:%M:%S")
    #------------------------------------------------------

    #Contenido de la consulta de agregación, se convierte el
    #formato de la fechaTweet en dias para que solo muestre el dia y
    #haga el sum por dia y por categoría
    pipeline=[
    { "$match": {'fechaTweet':{'$gte': ini, '$lte':  fin}}},
    {"$project": {"_id":0,"categoria":1,
                            "fechaTweet": { "$dateToString": { "format": "%d", "date": "$fechaTweet" } } }},
              {"$group":{"_id":{"categoria":"$categoria","fechaTweet":"$fechaTweet"},"total":{"$sum":1}}},
              {"$project": {"_id":0,"categoria":"$_id.categoria","dia":"$_id.fechaTweet", "total":"$total"}},
              {"$sort":{"dia":1}}]

    #Se pasa el contenido a la función de agregación
    tw=tweetsClasificados.aggregate(pipeline)

    return list(tw)
