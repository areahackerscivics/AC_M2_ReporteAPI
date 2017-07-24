#!/usr/bin/env python
# encoding: utf-8
#from bottle import route, run, template

import sys, os
import numpy as np
import datetime
parent_dir=os.getcwd()
path= os.path.dirname(parent_dir)
sys.path.append(path)

import json

import bottle
from bottle import route,run,request, response, static_file

from json import dumps

from BLL.distribucionBLL import getDistribucionBLL
from BLL.evolucionBLL import getEvolucionBLL
from BLL.topPalabrasBLL import getTopPalabrasBLL
from BLL.topHashtagssBLL import getTopHashtagsBLL
from BLL.catalogoBLL import getCatalogoBLL




# the decorator
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        """Habilitar solicitudes HTTP de sitios cruzados

            Permite a los servidores describir el conjunto de orígenes
            que tienen permiso de leer la información usando un explorador
            web.

            Access-Control-Allow-Origin:Específica una URI que puede tener
            acceso al recurso

            Access-Control-Allow-Methods:Específica el método o los métodos
            permitidos cuando se asigna un recurso.

            Access-Control-Allow-Headers:Usado en respuesta a una solicitud
            verificada para indicar cual encabezado HTTP puede ser usado
            cuando se realiza la solicitud real.
        """        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET'
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
    """Recupera un json con la distribución de tweets por categoría.

     GET devuelve una representación en JSON y un código de respuesta HTTP de 200 (OK).
     En caso de error, devuelve un 404 (NO ENCONTRADO) o 400 (BAD REQUEST).

     Ejemplo: http://localhost:8080/distribucion?anyo=2017&mes=07

    Respuesta:
    Status Code: 200 OK
    Access-Control-Allow-Headers: Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token
    Access-Control-Allow-Methods: GET
    Access-Control-Allow-Origin: *
    Content-Length: 1455
    Content-Type: application/json
    Date: Mon, 24 Jul 2017 14:13:16 GMT
    Server: WSGIServer/0.1 Python/2.7.11

    """
    response.content_type = 'application/json'

    anyo = request.query.anyo
    mes = request.query.mes

    result = getDistribucionBLL(anyo, mes)

    return dumps(result)



@app.route('/evolucion', method='GET')
@enable_cors
def evolucion():
    """Recupera un json con la evolución de tweets por categoría.

     GET devuelve una representación en JSON y un código de respuesta HTTP de 200 (OK).
     En caso de error, devuelve un 404 (NO ENCONTRADO) o 400 (BAD REQUEST).

     Ejemplo: http://localhost:8080/evolucion?anyo=2017&mes=03

    Respuesta:
    Status Code: 200 OK
    Access-Control-Allow-Headers: Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token
    Access-Control-Allow-Methods: GET
    Access-Control-Allow-Origin: *
    Content-Length: 2493
    Content-Type: application/json
    Date: Mon, 24 Jul 2017 14:18:33 GMT
    Server: WSGIServer/0.1 Python/2.7.11

    """
    response.content_type = 'application/json'

    anyo = request.query.anyo
    mes = request.query.mes

    result = getEvolucionBLL(anyo, mes)


    return dumps(result)


@app.route('/toppalabras', method='GET')
@enable_cors
def palabras():
    """Método no usado en esta version .
    """
    response.content_type = 'application/json'

    anyo = request.query.anyo
    mes = request.query.mes

    result = getTopPalabrasBLL(anyo, mes)

    return dumps(result)


@app.route('/tophashtags', method='GET')
@enable_cors
def hashtags():
    """Método no usado en esta version .
    """
    response.content_type = 'application/json'

    anyo = request.query.anyo
    mes = request.query.mes

    result = getTopHashtagsBLL(anyo, mes)

    return dumps(result)



@app.route('/catalogo', method='GET')
@enable_cors
def datasets():
    """Recupera un json con el número de datasets publicados por categoría.

     GET devuelve una representación en JSON y un código de respuesta HTTP de 200 (OK).
     En caso de error, devuelve un 404 (NO ENCONTRADO) o 400 (BAD REQUEST), del catálogo
     de datos abiertos publicado por el ayuntamiento de valencia.

     Ejemplo: http://localhost:8080//catalogo?anyo=2017&mes=07

    """

    response.content_type = 'application/json'

    result = getCatalogoBLL()

    return dumps(result)


#@app.route('/descarga/<filename:path>', method='GET')
@app.route('/descarga', method='GET')
@enable_cors
#def descarga(filename):
def descarga():
    anyo = request.query.anyo
    mes = request.query.mes

    filename = 'tweets_' + anyo + '_' + mes + '.json'

    if os.path.isfile("../FILES/"+filename):
        return static_file(filename, root='../FILES/', download=filename)
    else:
        result = getDistribucionBLL(anyo, mes)

        with open('../FILES/'+filename, 'wb') as fichero:
            json.dump(result, fichero)

        return static_file(filename, root='../FILES/', download=filename)





app.run(port=8080)
#bottle.run(host='localhost', port=8080)
