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





# the decorator
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


app = bottle.app()


# Query string is /distribucion?anyo=2017&mes=01
@app.route('/distribucion', method='GET')
@enable_cors
def distribucion():
    response.content_type = 'application/json'

    anyo = request.query.anyo
    mes = request.query.mes

    result = getDistribucionBLL(anyo, mes)

    return dumps(result)



@app.route('/evolucion', method='GET')
@enable_cors
def evolucion():
    response.content_type = 'application/json'

    anyo = request.query.anyo
    mes = request.query.mes

    result = getEvolucionBLL(anyo, mes)


    return dumps(result)


@app.route('/toppalabras', method='GET')
@enable_cors
def evolucion():
    response.content_type = 'application/json'

    anyo = request.query.anyo
    mes = request.query.mes

    result = getTopPalabrasBLL(anyo, mes)

    return dumps(result)


@app.route('/tophashtags', method='GET')
@enable_cors
def evolucion():
    response.content_type = 'application/json'

    anyo = request.query.anyo
    mes = request.query.mes

    result = getTopHashtagsBLL(anyo, mes)

    return dumps(result)



app.run(port=8080)
#bottle.run(host='localhost', port=8080)
