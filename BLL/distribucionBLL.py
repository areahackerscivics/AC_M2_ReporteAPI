#!/usr/bin/env python
# encoding: utf-8

import sys, os
import numpy as np
import datetime
parent_dir=os.getcwd()
path= os.path.dirname(parent_dir)
sys.path.append(path)

from DAO.tweetClasificadoDAO import *

def getDistribucionBLL(anyo, mes):
    """Devuelve el número de tweets por categoría.

     Retorna  un array con el  número de tweets por categoría, además
     de su porcentaje. En su proceso llama al  método que está en el DAO

     Parámetros:
     anyo: Año en el que fue creado el Tweet
     mes: Mes en el que fue creado el Tweet

    """
    #Se llama la DAO de los tweets clasificados
    tweets = getTweetsClasificados(anyo, mes)

    #Se inicializa el diccionario con los nombres de las categorías
    dicc = {
        'Ciencia y tecnología': 0,
        'Comercio': 0,
        'Cultura y ocio': 0,
        'Demografía': 0,
        'Deporte': 0,
        'Economía': 0,
        'Educación': 0,
        'Empleo': 0,
        'Energía': 0,
        'Hacienda': 0,
        'Industria': 0,
        'Legislación y justicia': 0,
        'Medio ambiente': 0,
        'Medio Rural': 0,
        'Salud': 0,
        'Sector público': 0,
        'Seguridad': 0,
        'Sociedad y bienestar': 0,
        'Transporte': 0,
        'Turismo': 0,
        'Urbanismo e infraestructuras': 0,
        'Vivienda': 0
    }

    for tweet in tweets:
        categoria = str(tweet['categoria'].encode('UTF-8'))
        #se realiza la suma de los tweets por categoría
        dicc[categoria] = dicc.get(categoria, 0) + 1

    #Se realiza la suma  total de los tweets clasificados
    totalTw = sum(dicc.values())

    result = []

    keys = list(dicc.keys())
    for key in keys:
        numTweets = dicc[key]
        if totalTw == 0:
            porTweets = 0.0
        else:
            #Se calcula el porcentaje por categoría
            porTweets = (numTweets/float(totalTw))*100
        result.append( {'categoria': key, 'numTweets': numTweets, 'porTweets': porTweets} )

    return result
