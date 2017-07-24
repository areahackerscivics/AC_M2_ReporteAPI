#!/usr/bin/env python
# encoding: utf-8

import sys, os
import numpy as np
import datetime
parent_dir=os.getcwd()
path= os.path.dirname(parent_dir)
sys.path.append(path)

import xml.dom.minidom
from xml.dom.minidom import parse

def getCatalogoBLL():
    """Devuelve el número de datasets por categoría.

     Retorna  un array con el nombre de la categoría con el número de
     datasets publicados por el ayuntamiento de valencia por categorías

     Nota: Se detectó que puede existir el mismo dataset en más de
     una categoría
    """

    DOMTree = xml.dom.minidom.parse('../FILES/catalogo.rdf')

    coleccion = DOMTree.documentElement

    #Se extrae el nombre de cada uno de los datasets
    datasets = coleccion.getElementsByTagName('dcat:dataset')

    print str(len(datasets))

    #Se inicializa el diccionario con los nombres de las temas (categorías)
    #como aparecen en el xml
    dicc = {
        'ciencia tecnologia': 0,
        'comercio': 0,
        'cultura ocio': 0,
        'demografia': 0,
        'deporte': 0,
        'economia': 0,
        'educacion': 0,
        'empleo': 0,
        'energia': 0,
        'hacienda': 0,
        'industria': 0,
        'legislacion justicia': 0,
        'medio ambiente': 0,
        'medio rural': 0,
        'salud': 0,
        'sector publico': 0,
        'seguridad': 0,
        'sociedad bienestar': 0,
        'transporte': 0,
        'turismo': 0,
        'urbanismo infraestructuras': 0,
        'vivienda': 0
    }

    for dataset in datasets:
        temas = dataset.getElementsByTagName('dcat:theme')
        for tema in temas:
            url =  tema.getAttribute('rdf:resource')
            catBruto = (url.split('/'))[-1]
            categoria = catBruto.replace('-', ' ')

            dicc[categoria] = dicc.get(categoria, 0) + 1


    result = []
    keys = dicc.keys()
    keys.sort()
    for categoria in keys:
        result.append( {'categoria': categoria, 'numDatasets': dicc[categoria]} )

    return result
