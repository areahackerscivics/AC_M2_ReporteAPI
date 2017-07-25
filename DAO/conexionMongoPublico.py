#!/usr/bin/env python
# encoding: utf-8

def getConexion():
    """Método que contine la cadena de conexión a la base de datos

    IMPORTANTE:
    Deberá crear la base de datos y en el return poner la cadena de conección 


    """

    return 'ruta de conexión a la base de datos'

#
def getDB():
    """Método que retorna el nombre de la BD que se está usando.
    """
    return 'db_tweets'

def getCollTweetsClas():
    """Devuelve el nombre de la colección Tweets Clasificados.

     Retorna el nombre de la colección que contiene los tweets
     clasificados.

     Justificación: Estos métodos se crear para que  sea fácil el
     mantenamiento del nombre de las colecciones.

    """
    return 'TWCLASIFICADO'
