#!/usr/bin/env python
# encoding: utf-8
from os import environ

def getConexion():
    """Método que contine la cadena de conexión a la base de datos

    La base de datos se encuentra alojada en mlab que es un servicio en la nube que
    hospeda BD de MongoDB
    """


    return environ.get("RUTA_MONGO")

#
def getCatalogo():
    return "CATALOGO"

def getDB():
    """Método que retorna el nombre de la BD que se está usando.
    """
    return 'db_tweets2018'

def getCollTweetsClas():
    """Devuelve el nombre de la colección Tweets Clasificados.

     Retorna el nombre de la colección que contiene los tweets
     clasificados.

     Justificación: Estos métodos se crear para que  sea fácil el
     mantenamiento del nombre de las colecciones.

    """
    return 'TWCLASIFICADO'
