#!/usr/bin/env python
# encoding: utf-8
#from bottle import route, run, template

import sys, os
import numpy as np
import datetime
parent_dir=os.getcwd()
path= os.path.dirname(parent_dir)
sys.path.append(path)

import bottle
from bottle import route,run,request, response

from json import dumps

from BLL.distribucionBLL import getDistribucionBLL
from BLL.evolucionBLL import getEvolucionBLL
from BLL.topPalabrasBLL import getTopPalabrasBLL
from BLL.topHashtagssBLL import getTopHashtagsBLL


# Query string is /distribucion?anyo=2017&mes=01
@route('/distribucion', method='GET')
def distribucion():
    response.content_type = 'application/json'

    anyo = request.query.anyo
    mes = request.query.mes

    result = getDistribucionBLL(anyo, mes)

    '''
    [
        {'categoria': key, 'numTweets': numTweets, 'porTweets': porTweets},
        {'categoria': key, 'numTweets': numTweets, 'porTweets': porTweets},
        ...
    ]
    '''
    return dumps(result)



@route('/evolucion', method='GET')
def evolucion():
    response.content_type = 'application/json'

    anyo = request.query.anyo
    mes = request.query.mes

    result = getEvolucionBLL(anyo, mes)


    return dumps(result)


@route('/toppalabras', method='GET')
def evolucion():
    response.content_type = 'application/json'

    anyo = request.query.anyo
    mes = request.query.mes

    result = getTopPalabrasBLL(anyo, mes)

    return dumps(result)


@route('/tophashtags', method='GET')
def evolucion():
    response.content_type = 'application/json'

    anyo = request.query.anyo
    mes = request.query.mes

    result = getTopHashtagsBLL(anyo, mes)

    return dumps(result)


'''
 # JSON format response
@route('/book/:id', method='GET')
def book():

    return {'id':id, 'name':'A Game of Thrones: A Song of Ice and Fire'}
'''



bottle.run(host='localhost', port=8080)
